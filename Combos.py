from tkinter import *
from tkinter import ttk 

root = Tk()

# var
estado = StringVar()

# Template
comboEstados = ttk.Combobox(root, textvariable=estado)
comboEstados.grid()
comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacán")

root.mainloop()