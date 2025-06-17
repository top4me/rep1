import toga

def build(app):
    # Просто создаем окно с текстом
    return toga.Label("Hello, World!")

if __name__ == '__main__':
    app = toga.App(
        name='Hello', 
        app_id='org.example.hello',
        startup=build
    )
    app.main_loop()