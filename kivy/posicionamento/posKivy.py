from kivy.app import App
from kivy.uix.floatlayout import FloatLayout 

#from kivy.uix.button import Button

class Root(FloatLayout):
    pass

class PosApp(App):

    def build(self):
        # return Button()
        return Root()


PosApp().run()
