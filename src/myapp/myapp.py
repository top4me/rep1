import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from jnius import autoclass  # Для доступа к Android API

def get_battery_status():
    try:
        # Используем Android API через PyJNIus
        Context = autoclass("android.content.Context")
        BatteryManager = autoclass("android.os.BatteryManager")
        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        
        activity = PythonActivity.mActivity
        battery_manager = activity.getSystemService(Context.BATTERY_SERVICE)
        
        # Получаем заряд батареи (в процентах)
        level = battery_manager.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
        
        # Проверяем, заряжается ли устройство
        is_charging = battery_manager.isCharging()
        
        status = "⚡ Заряжается" if is_charging else "🔋 Разряжается"
        return f"Заряд: {level}%\n{status}"
    
    except Exception as e:
        return f"Ошибка: {str(e)}"

def build(app):
    # Текстовое поле для вывода информации
    label = toga.Label(
        get_battery_status(),
        style=Pack(padding=10, font_size=16)
    
    # Кнопка для обновления данных
    button = toga.Button(
        "Обновить",
        on_press=lambda widget: setattr(label, "text", get_battery_status()),
        style=Pack(padding=5))
    
    # Главное окно
    box = toga.Box(
        children=[label, button],
        style=Pack(direction=COLUMN, padding=10))
    
    return box

def main():
    return toga.App(
        "Battery Monitor",
        "org.example.battery",
        startup=build)

if __name__ == "__main__":
    app = main()
    app.main_loop()