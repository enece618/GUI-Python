from tkinter import *
from tkinter import ttk 

# script
    # methods
def calcular(*args):
    try:
        resultado = float(pies.get()) * 0.3048 
        metros.set(resultado)
    except ValueError:
        metros.set(ValueError)
    

# template
raiz = Tk()
raiz.title("Pies a metros")

marcoPrincipal = ttk.Frame(raiz, padding="15 15 15 15")
marcoPrincipal.grid(column=0, row=0)

pies = StringVar()
metros= StringVar()

txtPies = ttk.Entry(marcoPrincipal, textvariable=pies)
txtPies.grid(row=0, column=1)

ttk.Label(marcoPrincipal, text="Pies").grid(row=0, column=2)
ttk.Label(marcoPrincipal, text="Son equivalentes a: ").grid(row=1, column=0)
ttk.Label(marcoPrincipal, textvariable=metros).grid(row=1, column=1)
ttk.Label(marcoPrincipal, text="Metros").grid(row=1, column=2)

ttk.Button(marcoPrincipal, text="Calcular", command=calcular).grid(row=2, column=2)

for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=5, pady=5)

txtPies.focus()
raiz.bind("<Return>", calcular)

raiz.mainloop()
