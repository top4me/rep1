import toga
from toga.style import Pack
from toga.style.pack import COLUMN

class MyApp(toga.App):
    def startup(self):
        box = toga.Box(style=Pack(direction=COLUMN))
        label = toga.Label("Hello, World!")
        box.add(label)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = box
        self.main_window.show()

def main():
    return MyApp("MyApp", "com.example.myapp")

if __name__ == "__main__":
    main().main_loop()
