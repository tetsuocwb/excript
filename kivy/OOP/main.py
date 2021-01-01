from kivy.app import App
from kivy.uix.label import Label


class segundo(App):
    
    def build(self):
        #print(self.__dict__)
        return Label()


def main():
    segundo().run()


segundo().run()