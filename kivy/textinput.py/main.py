from kivy.app import App
from kivy.uix.textinput import TextInput

# class AppTitle(App):
#     def __init__(self, **kwargs):
#         super(AppTitle, self).__init__(**kwargs)
        
def onEnter(instance, value):
    #x = value
    #print('dasdfaasdfasdfa')
    print(value, instance)


def build():
    entrada = TextInput()
    entrada.text = 'dsfa'
    entrada.multiline = False
    entrada.password = True
    entrada.bind(on_text_validate = onEnter)
    #entrada.bind(text = onEnter)
    
    return entrada

janela = App()
janela.build = build
janela.run()


