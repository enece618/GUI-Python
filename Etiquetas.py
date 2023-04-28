from tkinter import *
from tkinter import ttk

root = Tk()

labelTxt = ttk.Label(root, text="Etiqueta solo texto")
labelTxt.grid()

img = PhotoImage(file="pikachu_pixel.png")

labelImg = ttk.Label(root)
labelImg.grid()
labelImg['image'] = img

labelCombined = ttk.Label(root, text="Etiqueta combinada", compound="center")
labelCombined.grid()
labelCombined['image'] = img

root.mainloop()