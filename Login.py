from tkinter import *
from tkinter import ttk 
from tkinter import messagebox

# script
    
    # methods
def loggin(*args):
    messagebox.showinfo(message="Se inició sesión.", title="Inicio de sesión")

# template
root = Tk()
root.title("Inicio de sesión")

#var
usuario = StringVar()
contraseña= StringVar()

ttk.Label(root, text="Usuario:").grid(pady=5, row=0, column=0)
ttk.Label(root, text="Contraseña:").grid( pady=5, row=1, column=0)

ttk.Entry(root, width=40, textvariable=usuario).grid(padx=5, row=0, column=1)
ttk.Entry(root, width=40, show="*", textvariable=contraseña).grid(padx=5, row=1, column=1)

ttk.Button(root, text="Aceptar", width=50, command=loggin).grid(padx=10, pady=10, row=2, column=0, columnspan=2)

root.mainloop()