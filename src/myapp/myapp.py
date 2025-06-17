import toga
from android.config import JAVA_NAMESPACE
from android.permissions import request_permissions, Permission

def build(app):
    try:
        # Запрашиваем обязательные разрешения
        request_permissions([Permission.INTERNET])
        
        # Минимальный интерфейс
        box = toga.Box()
        label = toga.Label("Приложение запущено!", style=dict(padding=50))
        box.add(label)
        return box
        
    except Exception as e:
        # Записываем ошибку в логи Android
        from android.util import Log
        Log.e("TogaApp", f"Startup error: {str(e)}")
        raise

if __name__ == '__main__':
    app = toga.App(
        'MyApp',
        'com.example.myapp',
        startup=build,
        # Обязательные параметры для Android
        icon='resources/icon',
        version='1.0',
        description='Test App'
    )
    app.main_loop()