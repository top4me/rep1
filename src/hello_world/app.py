 
import toga

def button_handler(widget):
    print("Hello World!")

def build(app):
    box = toga.Box()
    button = toga.Button("Click me!", on_press=button_handler)
    box.add(button)
    return box

def main():
    return toga.App("Hello World", "org.example.helloworld", startup=build)