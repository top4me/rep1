import toga

def build(app):
    return toga.Box(children=[
        toga.Label("Hello World!", style=Pack(padding=20))
    ])

def main():
    return toga.App(
        formal_name="MyApp",
        app_id="org.example.myapp",
        startup=build
    )