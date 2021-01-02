from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
# class AppTitle(App):
#     def __init__(self, **kwargs):
#         super(AppTitle, self).__init__(**kwargs)
        
def clique():
    print(ed.text)

def build():
    
    layout = FloatLayout()
    global ed
    ed = TextInput(text='tetsuo')
    ed.size_hint = None, None
    ed.height = 300
    ed.width = 400
    ed.x=60
    ed.y=250

    bt = Button(text='click')
    bt.size_hint = None, None
    bt.height = 50
    bt.width = 200
    bt.x=150
    bt.y=170
    bt.on_press = clique
    
    
    layout.add_widget(ed)
    layout.add_widget(bt)
    return layout


janela = App()
janela.title = "First App"
from kivy.core.window import Window
Window.size = 600,600



janela.build = build
janela.run()