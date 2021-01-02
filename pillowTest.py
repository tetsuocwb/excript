from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('foto')
# my_img = ImageTk.PhotoImage(Image.open('B2A2A9D5-B3C2-4BE1-95B5-F466CB3CFDAC_1_105_c.jpeg'))
# my_label = Label(image = my_img)
# my_label.grid(row = 0, column = 0)


imagem = Image. open('B2A2A9D5-B3C2-4BE1-95B5-F466CB3CFDAC_1_105_c.jpeg')
imagem = imagem.resize((450, 350), Image.ANTIALIAS)
imagemtk = ImageTk.PhotoImage(imagem)
# my_img1 = ImageTk.PhotoImage(Image.open('B2A2A9D5-B3C2-4BE1-95B5-F466CB3CFDAC_1_105_c.jpeg'))
# my_label1 = Label(image = my_img1)
my_label1 = Label(image = imagemtk)

my_label1.grid(row = 0, column = 1)
# image1 = Image.open('B2A2A9D5-B3C2-4BE1-95B5-F466CB3CFDAC_1_105_c.jpeg')
# image1.show()

root.mainloop()