import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from java.lang import Class
from android.permissions import request_permissions, Permission
from java import jarray

SensorManager = None
Sensor = None
Context = None

class SensorApp(toga.App):
    def startup(self):
        global SensorManager, Sensor, Context

        # Запрашиваем разрешения
        request_permissions([Permission.BODY_SENSORS])

        # Получаем текущую NativeActivity
        activity = self._impl.native_activity
        Context = Class.forName("android.content.Context")
        sensor_service = activity.getSystemService(Context.SENSOR_SERVICE)

        # Получаем классы сенсоров
        SensorManager = Class.forName("android.hardware.SensorManager")
        Sensor = Class.forName("android.hardware.Sensor")

        # Получаем список всех сенсоров
        sensor_list = sensor_service.getSensorList(Sensor.TYPE_ALL)

        sensor_names = []
        for i in range(sensor_list.size()):
            sensor = sensor_list.get(i)
            sensor_names.append(sensor.getName())

        # Показываем в интерфейсе
        self.label = toga.Label("\n".join(sensor_names), style=Pack(padding=10))
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = toga.Box(children=[self.label], style=Pack(direction=COLUMN))
        self.main_window.show()


def main():
    return SensorApp("Sensor App", "com.example.sensorapp")