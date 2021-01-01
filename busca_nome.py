from tkinter import *
from fuzzywuzzy import process, fuzz
import xlrd

book = xlrd.open_workbook("/Users/tetsuo/dev/python/Relacaodegalerias.xls")
gal = book.sheet_by_name("GAL-CUB")
todosNomes = gal.col_values(4)

selecao = [("","")]
lista = ['tetsuo', 'lucas', 'pamela']
entrada = []
box = "vazio"


def procura_nome(nome , iterab):
    lista_nomes = list(map(str, iterab))
    print(" ")

def ler(event):
#    print(event.char)
    # global box
    # global selecao
    box = e.get()
    selecao = process.extractBests(box, todosNomes, scorer = fuzz.partial_token_sort_ratio , limit = 5)
    print(selecao[0][0])
    # retorno()
    nomes.configure(text = selecao) # atualiza message oou label no tinker

def sair(event):
    exit()

def retorno():
    global box
    nomes = Label(root, text = selecao)
    nomes.pack()
    print(box, "retorno")

root = Tk()

e = Entry(root, width = 45)
e.pack()
e.bind("<KeyRelease>" , ler)
# for i in lista:
#     nome+i = Label(root, text = lista[i])
#     char(93+i).pack()
nomes = Message(root, text = selecao)
nomes.pack()

# retorno()

e.bind('<Escape>', sair)


root.mainloop()

