import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from rubicon.java import JavaClass, JavaInterface, java_method, cast
from jnius import autoclass

# Android sensor classes
Context = autoclass('android.content.Context')
SensorManager = autoclass('android.hardware.SensorManager')
Sensor = autoclass('android.hardware.Sensor')
SensorEventListener = JavaInterface('android.hardware.SensorEventListener')

class MySensorListener(JavaClass, implements=[SensorEventListener]):
    __javainterfaces__ = ['android/hardware/SensorEventListener']
    __javacontext__ = 'app'

    def __init__(self, label):
        super().__init__()
        self.label = label

    @java_method('(Landroid/hardware/SensorEvent;)V')
    def onSensorChanged(self, event):
        values = [str(v) for v in event.values.toArray()]
        sensor_type = event.sensor.getType()
        text = f"Sensor {sensor_type}: {', '.join(values)}"
        # Обновляем UI в главном потоке
        toga.App.app.main_window.content.children[0].text = text

    @java_method('(Landroid/hardware/Sensor;I)V')
    def onAccuracyChanged(self, sensor, accuracy):
        pass

def build(app):
    # UI
    label = toga.Label("Waiting for sensor data...", style=Pack(padding=10))
    box = toga.Box(children=[label], style=Pack(direction=COLUMN, padding=10))

    # Android context
    PythonActivity = autoclass('org.beeware.android.MainActivity')
    context = PythonActivity.mActivity.getSystemService(Context.SENSOR_SERVICE)
    sensor_manager = cast('android.hardware.SensorManager', context)

    # Выбор всех доступных сенсоров
    sensors = sensor_manager.getSensorList(Sensor.TYPE_ALL)

    # Запускаем прослушивание
    listener = MySensorListener(label)
    for sensor in sensors.toArray():
        sensor_manager.registerListener(listener, sensor, SensorManager.SENSOR_DELAY_UI)

    return box

def main():
    return toga.App("Sensor Reader", "com.example.sensors", startup=build)