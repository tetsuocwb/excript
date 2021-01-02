from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class segundo(App):
    
    def build(self):
        #print(self.__dict__)
        Window.bind(on_dropfile=self.on_drop)
        return 

    def on_drop(self,window, file_path):
        print(file_path)
        return


segundo().run()