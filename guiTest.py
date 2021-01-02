from tkinter import *
root = Tk()
L1 = Label(root, text = "Nome")
L1.pack(side = LEFT)
e = Entry(root, width = 50)
e.pack()
y = ""
def entrada(event):
    ent = e.get()
    e.delete(0, END)
    e.insert(0, 'oi, ' + ent)
    #e.insert(0, "foi " + e.get())


e.bind('<Return>', entrada)

def sair(event):
    exit()


e.bind('<Escape>', sair)



root.mainloop()