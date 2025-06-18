import toga; from jnius import autoclass as a
def build(app):
 r=a('org.beeware.android.MainActivity').singletonThis.getApplicationContext().registerReceiver(None,a('android.content.IntentFilter')(a('android.content.Intent').ACTION_BATTERY_CHANGED))
 return toga.Box(children=[toga.Label(f"🔋 {int(r.getIntExtra('level',-1)/r.getIntExtra('scale',-1)*100)}%")])
def main(): return toga.App("B","com.example.myapp.myapp",startup=build)