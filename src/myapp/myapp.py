import toga; from jnius import autoclass as a
def build(app):
 c=a('org.beeware.android.MainActivity').singletonThis.getApplicationContext()
 r=c.registerReceiver(None, a('android.content.IntentFilter')(a('android.content.Intent').ACTION_BATTERY_CHANGED))
 t="⚠" if not r else f"🔋 {int(r.getIntExtra('level',-1)/r.getIntExtra('scale',-1)*100)}%"
 return toga.Box(children=[toga.Label(t)])
def main(): return toga.App("B","com.example.myapp.myapp",startup=build)