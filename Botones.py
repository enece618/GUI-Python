from tkinter import *
from tkinter import ttk 

root = Tk()

button = ttk.Button(root, text="Botón solo de texto")
button.grid()

img = PhotoImage(file="pikachu_pixel.png")

btnImg = ttk.Button(root)
btnImg.grid()
btnImg['image'] = img

btnCombinated = ttk.Button(root, text="Botón combinado", compound="bottom")
btnCombinated.grid()
btnCombinated['image'] = img

chkButton = ttk.Checkbutton(root, text="Opcion 1")
chkButton.grid()

root.mainloop()