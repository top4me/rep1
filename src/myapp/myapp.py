import toga
def build(app): return toga.Label("Hello!")
app = toga.App("Test", "com.test.app", startup=build)
app.main_loop()