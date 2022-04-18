from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder

KV = """

#:import win kivy.core.window

<Picture@Scatter>:
    source: None
    on_size: self.center = win.Window.center
    size: fard.size
    size_hint: None, None   
    Image:
        id: fard
        size: 50,20
        source: root.source 
FloatLayout:
    Picture:
        source: "test.jpg"
    Picture:
        source: "test.jpg"

"""

class MyApp(App):

    def build(self):
        return Builder.load_string(KV)

MyApp().run()