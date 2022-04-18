from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.behaviors import DragBehavior
from kivy.uix.boxlayout import BoxLayout


class Box_layout(BoxLayout):
    def __init__(self,**kwargs):
        super(Box_layout, self).__init__(**kwargs)
        self.size_hint = (.50,.50)
        self.orientation = "vertical"
        for  x in range(5):
           DragButton.text=str(x)
           self.add_widget(DragButton())

class DragButton(DragBehavior, Button):
    def __init__(self,**kwargs):
       super(DragButton, self).__init__(**kwargs)
       self.drag_rect_width = 1366
       self.drag_rect_height = 768
       self.drag_timeout = 10000000
       self.drag_distance = 0
       print(self.height, self.width)
class atry(App):
    def build(self):
        return DragButton()
atry.run()