from kivy.app import App
from kivy.uix.label import Label 

def build():
    # return Label(text = "Curso python e kivy", italic = True)
    lb =Label()
    lb.text = "Curso de Python and Kivy"
    lb.italic = True
    lb.font_size = 50
    return lb
app = App()
app.build = build
app.run()