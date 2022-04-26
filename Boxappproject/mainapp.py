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
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")
conn = False
if conn == True: 
    c, addr = s.accept()
    print("past")   
    print ('Got connection from', addr)
    # send a thank you message to the client. encoding to send byte type.
    c.send('Thank you for connecting'.encode())
    print(c.recv(1024).decode())
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

Window.size = (900, 800)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

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
class TabbedPanelApp(App):
    def ball_move(self, dt):
    

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
        print("-"*10)
        print(name)
        
        kivids = self.root.ids
        wids = [[kivids.Time,[50,100]],[kivids.Song,[175,100]]]
        count+=1
        widx,widy = wid.pos
        print(widx,widy)
        tleft = self.root.ids.tleft
        tright = self.root.ids.tright
        bleft = self.root.ids.bleft
        bright = self.root.ids.bright
        center = self.root.ids.center
        #if widx > 

        if widx > tleft.pos[0]-99 and widx < tleft.pos[0]+250:
            if widy > tleft.pos[1]-39 and widy < tleft.pos[1]+150:
                print("collided tleft")
                if conn == True:
                    c.send(("1-"+name).encode())
        if widx > tright.pos[0]-99 and widx < tright.pos[0]+250:
            if widy > tright.pos[1]-39 and widy < tright.pos[1]+150:
                print("collided tright")
                if conn == True:
                    c.send(("2-"+name).encode())
        if widx > center.pos[0]-99 and widx < center.pos[0]+350:
            if widy > center.pos[1]-39 and widy < center.pos[1]+200:
                print("collided center")
                if conn == True:
                    c.send(("0-"+name).encode())            
        if widx > bright.pos[0]-99 and widx < bright.pos[0]+250:
            if widy > bright.pos[1]-39 and widy < bright.pos[1]+150:
                print("collided bright")
                if conn == True:
                    c.send(("4-"+name).encode())
        if widx > bleft.pos[0]-99 and widx < bleft.pos[0]+250:
            if widy > bleft.pos[1]-39 and widy < bleft.pos[1]+150:
                print("collided bleft")
                if conn == True:
                    c.send(("3-"+name).encode())
        for wid in wids:
            wid[0].pos = wid[1]
    def change(self):
        but1 = self.root.ids.jon.text
        print(but1)
    #Use init to run stuff on startup
    def build(self):
        Clock.schedule_interval(self.ball_move,1)
        print("x"*100)
        return Test()
TabbedPanelApp().run()

