import toga

def main():
    return toga.App("Hello", "org.example.hello", startup=lambda app: (
        (w := toga.MainWindow(title=app.formal_name)),
        w.set_content(toga.Label("Hello, world!", style={"padding": 20})),
        w.show()
    )[-1])  # Возвращаем App

if __name__ == "__main__":
    main().main_loop()