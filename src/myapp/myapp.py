import toga
from android.permissions import request_permissions, Permission

def build(app):
    request_permissions([Permission.INTERNET])
    return toga.Box(children=[toga.Label("Hello!")])

app = toga.App("Test", "com.example.testapp", startup=build)
app.main_loop()