import toga

def build(app):
    return toga.Box(children=[toga.Label("Hello from Toga!")])

def main():
    return toga.App("TestApp", "com.example.testapp", startup=build)