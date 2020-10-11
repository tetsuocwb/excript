from tkinter import *

def procura_nome(nome , iterab):
    lista_nomes = list(map(str, iterab))
    print(" ")

def ler(event):
    print(event.char)

lista = ['tetsuo', 'lucas', 'pamela']
entrada = []
root = Tk()

e = Entry(root, width = 45)
e.pack()
e.bind("<Key>" , ler)
# for i in lista:
#     nome+i = Label(root, text = lista[i])
#     char(93+i).pack()
nomes = Message(root, text = lista)
nomes.pack()



root.mainloop()

