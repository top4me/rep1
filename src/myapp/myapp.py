import toga
import psutil
import os
import sys
from toga.style import Pack
from toga.style.pack import COLUMN

def get_battery_status():
    try:
        battery = psutil.sensors_battery()
        if battery:
            return f"🔋 Заряд: {battery.percent}% | {'⚡ Зарядка' if battery.power_plugged else '🔌 Разряжается'}"
        return "Батарея не обнаружена"
    except Exception as e:
        return f"Ошибка: {str(e)}"

def build(app):
    battery_label = toga.Label(get_battery_status(), style=Pack(font_size=14, padding=10))
    button = toga.Button(
        "Обновить",
        on_press=lambda widget: setattr(battery_label, 'text', get_battery_status()),
        style=Pack(padding=5)
    )
    box = toga.Box(children=[battery_label, button], style=Pack(direction=COLUMN, padding=10))
    return box

def main():
    return toga.App(
        "Battery Monitor",
        "org.example.batterymonitor",
        startup=build,
        backend='gtk',  # Или другой бэкенд
    )

if __name__ == "__main__":
    if os.getenv('CI') == 'true':
        print(get_battery_status())
        sys.exit(0)
    try:
        app = main()
        app.main_loop()
    except Exception as e:
        print(f"CRASH: {e}", file=sys.stderr)
        sys.exit(1)