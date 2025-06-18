import toga
import psutil

def get_battery_status():
    battery = psutil.sensors_battery()
    if battery:
        return f"🔋 Заряд: {battery.percent}% | {'⚡ Зарядка' if battery.power_plugged else '🔌 Не заряжается'}"
    return "Батарея не обнаружена"

def build(app):
    # Обновляемое поле с зарядом батареи
    battery_label = toga.Label(get_battery_status(), style=Pack(font_size=14, padding=10))
    
    # Кнопка для обновления
    button = toga.Button(
        "Обновить",
        on_press=lambda widget: battery_label.text = get_battery_status(),
        style=Pack(padding=5)
    )
    
    # Основной контейнер
    box = toga.Box(
        children=[battery_label, button],
        style=Pack(direction=COLUMN, padding=10)
    )
    return box

def main():
    return toga.App(
        "Battery Monitor",
        "org.example.batterymonitor",
        startup=build,
        icon="icons/battery.ico"  # (опционально) путь к иконке
    )

if __name__ == "__main__":
    app = main()
    app.main_loop()