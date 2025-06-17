 
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

class MyApp(toga.App):
    def startup(self):
        box = toga.Box(style=Pack(direction=COLUMN))
        button = toga.Button('Click me', on_press=self.say_hello)
        box.add(button)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = box
        self.main_window.show()

    def say_hello(self, widget):
        print("Hello, Toga!")

def main():
    return MyApp('Hello Toga', 'org.example.hellotoga')

if __name__ == '__main__':
    main().main_loop()