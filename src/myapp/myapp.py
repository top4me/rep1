import toga
from jnius import autoclass

def get_battery_level():
    # Получаем контекст Android-приложения
    PythonActivity = autoclass('org.beeware.android.MainActivity')
    Intent = autoclass('android.content.Intent')
    IntentFilter = autoclass('android.content.IntentFilter')
    BatteryManager = autoclass('android.os.BatteryManager')

    activity = PythonActivity.singletonThis
    context = activity.getApplicationContext()

    ifilter = IntentFilter(Intent.ACTION_BATTERY_CHANGED)
    battery_status = context.registerReceiver(None, ifilter)

    level = battery_status.getIntExtra(BatteryManager.EXTRA_LEVEL, -1)
    scale = battery_status.getIntExtra(BatteryManager.EXTRA_SCALE, -1)

    battery_pct = int((level / scale) * 100)
    return f"Заряд батареи: {battery_pct}%"

def build(app):
    battery_text = get_battery_level()
    return toga.Box(children=[toga.Label(battery_text)])

def main():
    return toga.App("BatteryApp", "com.example.myapp", startup=build)