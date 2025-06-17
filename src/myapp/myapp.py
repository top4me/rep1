import toga
from android.permissions import request_permissions, Permission

def build(app):
    request_permissions([Permission.INTERNET])
    return toga.Box(children=[toga.Label("Hello!")])

def main():
    return toga.App("Test", "com.example.testapp", startup=build)