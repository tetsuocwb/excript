from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
<<<<<<< HEAD
from kivy.uix.label import Label
=======
>>>>>>> 6c8014e3575b347590bf03dcaf67bcb657b58508
import time
from kivy.clock import Clock
import datetime
import threading

inicio = time.perf_counter()
current = None
class temporizadorApp(App):
    def build(self):
        
        return Root()

class Root(FloatLayout):
    
    print (inicio)
    
    

    def elapsed(self):
        global current
        current = time.perf_counter()
        print(current - inicio)
        
        #t =self.atualiza()


    def atualiza(self):
        
        current = time.perf_counter()
        now = datetime.datetime.now()
        self.ids.tempo.text = now.strftime("%H:%M:%S") #str(current)
    
    while True:
        self.atualiza()
        time.sleep(1)
    #f = Clock.schedule_interval(atualiza , 1)
    
    
#f = Root()
# f.elapsed()






temporizadorApp().run()