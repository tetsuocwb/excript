from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
import time
from kivy.clock import Clock
import datetime
import threading
from kivy.properties import ObjectProperty,StringProperty

inicio = time.perf_counter()
current = None

class temporizadorApp(App):
    def build(self):
        xyz= Base()
        clocktext = xyz.ids.clocktext
        #clock = Atualiza()
        Clock.schedule_interval(clocktext.atual , 1)
        return xyz

class ClockText(Label):
        def atual(self, *args):
            current = time.perf_counter()
            now = datetime.datetime.now()
            #self.ids.tempo.text = now.strftime("%H:%M:%S") #str(current)
            #self.elapsed_time = str(current - inicio)
            print("f")
            self.text = "test"

class Base(FloatLayout):
    elapsed_time = StringProperty()
    print (inicio)
    lab = ObjectProperty(None)
    
    

    def elapsed(self):
        global current
        current = time.perf_counter()
        print(current - inicio)
        self.elapsed_time = str(current - inicio)
        #t =self.atualiza()


    # def atualiza(self):
        
    #     current = time.perf_counter()
    #     now = datetime.datetime.now()
    #     #self.ids.tempo.text = now.strftime("%H:%M:%S") #str(current)
    #     #self.elapsed_time = str(current - inicio)
    #     print("f")
    #     self.lab.text = "test"
    
    # while True:
    #     self.atualiza()
    #     time.sleep(1)
#f = Clock.schedule_interval(Root.atualiza , 1)
    
    
#f = Root()
# f.elapsed()






temporizadorApp().run()