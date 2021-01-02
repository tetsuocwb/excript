from tkinter import *
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import xlrd
import difflib
root = Tk()
e = Entry(root, width=100)
e.bind('<Key-Return>')
e.pack()

book = xlrd.open_workbook("/Users/tetsuo/dev/python/Relacaodegalerias.xls")
gal = book.sheet_by_name("GAL-CUB")
#nomet = gal.col_values(4)
#print(nomet)
aprox = []
preso = "DIEGO"
def prep_tabela(tab): # Uppercase de todas strings, remove espaços desnecessarios,
    tabela = []
    for a in tab:
        if str(a)[0] == " ":
            print(a)
        tabela.append(str(a))
        xyz = "tets"
    return tabela

nome = prep_tabela(gal.col_values(4))
#print(nome[2])
#print(aprox)
#P2 = []
P1 = process.extract(preso, aprox, limit=20)
#print("resultado", P1, "FIM")
# for a in P1:
#     if preso in a[0]:
#         P2.append(a[0])
# print(P2)
# #print(difflib.get_close_matches("DIEGO H", P2, 3, 0.6))
# x = P1[1][0]
# print("DIEGO" in x)
root.mainloop()