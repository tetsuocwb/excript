# coding: utf-8

from kivy.app import App
from kivy.uix.button import Button 

def clique():
    print("pressionou")

def build():

    bt = Button(text = "2")
    #bt.text = "Clique"
    bt.on_press = clique
    return bt

janela = App()
janela.build =build
janela.run()