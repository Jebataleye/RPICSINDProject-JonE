# first of all import the socket library
import socket            
 
# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network

conn = True
if conn == True: 
    s.connect(('127.0.0.1', port))

    message = input("Enter a message: ")
    s.send(message.encode())
    # receive data from the server and decoding to get the string.
# close the connection
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.behaviors import DragBehavior
from kivy.core.window import Window
from kivy.uix.scatter import Scatter
from kivy.uix.anchorlayout import AnchorLayout
from matplotlib.widgets import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.clock import Clock

Window.size = (800, 480)
Window.borderless = True
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
Config.set('graphics', 'resizable', False)
class Picture(Scatter): 
    t = ObjectProperty(None)
    pass
class DragLabel(DragBehavior, Label):
    pass
class Test(BoxLayout):
    pass
class ScatterWidget(Scatter):
    pass
class ScatterWid(Widget):
    pass
count = 0
ballvel = [1,1]
class Pisection(App):
    def ball_move(self, dt):
        if conn==True:
            message = s.recv(1024).decode()
            print (message)
            message = message.split("-")
            prefix = message[0]
            content = message[1]
            if prefix == 1:
                self.root.ids.tleft.text = content
                

        ball = self.root.ids.ball
        if ball.pos[0]>800 or ball.pos[0] == 800 or ball.pos[0] < 0:
            ballvel[0] *= -1
        if ball.pos[1]>550 or ball.pos[1]==550 or ball.pos[1]<0:
            ballvel[1]*=-1
        ball.pos[0]+=ballvel[0]
        ball.pos[1]+=ballvel[1]
        
    
    def start(self):
        global a 
        a = self.root.ids.jon.text
        print(a,"xl") 
    
    def functest(self,wid,name):
        global count
        print(name,count)
        print(wid.pos)
        count+=1
    def change(self):
        but1 = self.root.ids.jon.text
        print(but1)
    #Use init to run stuff on startup
    def build(self):
        Clock.schedule_interval(self.ball_move,1)
        print("x"*100)
        return Test()
Pisection().run()

