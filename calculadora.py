from tkinter import *
root = Tk()
root.title("Calculadora")
PADBUTTON = 33
expressao = []

e = Entry(root, width = 35)
e.grid(row=0, column=0, columnspan=3)

def numero(n):
    anterior = e.get()
    e.delete(0, END)
    e.insert(0, anterior + str(n))

    return


def adicao():
    x = e.get()
    e.delete(0, END)
    expressao.append(x)
    expressao.append("+")
    return

def limpa():
    e.delete(0, END)
    expressao.clear()
    return

def igual():
    expressao.append(e.get())
    e.delete(0, END)
    q =0
    for i in expressao:
        if i == "":
            expressao[q] = "0"
        q += 1
    e.insert(0, eval(" ".join(expressao)))
    expressao.clear() # limpa a expressao para ser possivel efetuar outra operacao e usar o resultado
    return

def multiplica():
    x = e.get()
    e.delete(0, END)
    expressao.append(x)
    expressao.append("*")
    return

def subtrai():
    x = e.get()
    e.delete(0, END)
    expressao.append(x)
    expressao.append("-")
    return

def divide():
    x = e.get()
    e.delete(0, END)
    expressao.append(x)
    expressao.append("/")
    return


button_1 = Button(root, padx = PADBUTTON, pady = 10, text = "1", command = lambda: numero(1))
button_2 = Button(root, padx = PADBUTTON, pady = 10, text = "2", command = lambda: numero(2))
button_3 = Button(root, padx = PADBUTTON, pady = 10, text = "3", command = lambda: numero(3))
button_4 = Button(root, padx = PADBUTTON, pady = 10, text = "4", command = lambda: numero(4))
button_5 = Button(root, padx = PADBUTTON, pady = 10, text = "5", command = lambda: numero(5))
button_6 = Button(root, padx = PADBUTTON, pady = 10, text = "6", command = lambda: numero(6))
button_7 = Button(root, padx = PADBUTTON, pady = 10, text = "7", command = lambda: numero(7))
button_8 = Button(root, padx = PADBUTTON, pady = 10, text = "8", command = lambda: numero(8))
button_9 = Button(root, padx = PADBUTTON, pady = 10, text = "9", command = lambda: numero(9))
button_0 = Button(root, padx = PADBUTTON, pady = 10, text = "0", command = lambda: numero(0))

button_add = Button(root, padx = 89, pady = 10, text = "+", command = adicao)
button_clear = Button(root, padx = 22, pady = 10, text = "Clear", command = limpa)
button_equal = Button(root, padx = 89, pady = 10, text = "=", command = igual)
button_mult = Button(root, padx = PADBUTTON, pady = 10, text = "x", command = multiplica)
button_sub = Button(root, padx = PADBUTTON, pady = 10, text = "-", command = subtrai)
button_div = Button(root, padx = PADBUTTON, pady = 10, text = "/", command = divide)

button_9.grid(row = 1, column = 2)
button_8.grid(row = 1, column = 1)
button_7.grid(row = 1, column = 0)

button_6.grid(row = 2, column = 2)
button_5.grid(row = 2, column = 1)
button_4.grid(row = 2, column = 0)

button_3.grid(row = 3, column = 2)
button_2.grid(row = 3, column = 1)
button_1.grid(row = 3, column = 0)

button_0.grid(row = 4, column = 0)

button_add.grid(row = 4, column = 1, columnspan = 2)
button_clear.grid(row = 6, column = 0)
button_equal.grid(row = 6, column = 1, columnspan = 2)
button_mult.grid(row = 7, column = 0)
button_div.grid(row = 7, column = 1)
button_sub.grid(row = 7, column = 2)

root.mainloop()
