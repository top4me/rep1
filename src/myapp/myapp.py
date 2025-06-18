import toga
import sys
import os
from toga.style import Pack
from toga.style.pack import COLUMN

# Выберите подходящий метод для вашей ОС!
def get_battery_status():
    try:
        # Вариант для Windows (ctypes)
        import ctypes
        class SYSTEM_POWER_STATUS(ctypes.Structure):
            _fields_ = [
                ("ACLineStatus", ctypes.c_byte),
                ("BatteryFlag", ctypes.c_byte),
                ("BatteryLifePercent", ctypes.c_byte),
            ]
        status = SYSTEM_POWER_STATUS()
        if ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.pointer(status)):
            percent = status.BatteryLifePercent
            if percent != 255:
                return f"🔋 Заряд: {percent}%"
        return "Батарея не найдена"
    except Exception as e:
        return f"Ошибка: {str(e)}"

def build(app):
    label = toga.Label(get_battery_status(), style=Pack(padding=10))
    button = toga.Button(
        "Обновить",
        on_press=lambda widget: setattr(label, 'text', get_battery_status()),
    )
    box = toga.Box(children=[label, button], style=Pack(direction=COLUMN))
    return box

def main():
    return toga.App(
        "Battery Monitor",
        "org.example.batterymonitor",
        startup=build,
        backend='winforms',  # Или 'gtk', 'cocoa'
    )

if __name__ == "__main__":
    try:
        app = main()
        app.main_loop()
    except Exception as e:
        print(f"CRASH: {e}", file=sys.stderr)
        sys.exit(1)