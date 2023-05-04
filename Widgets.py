from tkinter import *
from tkinter import ttk 

root = Tk()
root.title("Muestra Widgets")

estado = StringVar()

backgroundFrame = ttk.Frame(root, padding="15 15 15 15")
backgroundFrame.grid(row=1, column=0)

inputFrame = ttk.Frame(backgroundFrame, relief="raised", padding="20 20 20 20")
inputFrame.grid(row=0, column=0, padx=20, pady=20)
ttk.Label(inputFrame, text="Nombre").grid(row=0, column=0, sticky=W)
ttk.Entry(inputFrame).grid(row=0, column=1, sticky=E)
ttk.Label(inputFrame, text="A. Paterno").grid(row=1, column=0, sticky=W)
ttk.Entry(inputFrame).grid(row=1, column=1, sticky=E)
ttk.Label(inputFrame, text="A. Paterno").grid(row=2, column=0, sticky=W)
ttk.Entry(inputFrame).grid(row=2, column=1, sticky=E)
ttk.Label(inputFrame, text="Correo").grid(row=3, column=0, sticky=W)
ttk.Entry(inputFrame).grid(row=3, column=1, sticky=E)
ttk.Label(inputFrame, text="Movil").grid(row=4, column=0, sticky=W)
ttk.Entry(inputFrame).grid(row=4, column=1, sticky=E)

for input in inputFrame.winfo_children():
    input.grid_configure(padx=10, pady=10)

radioFrame = ttk.Frame(backgroundFrame, padding="20 20 20 20")
radioFrame.grid(row=0, column=1)
radioBtn1 = ttk.Radiobutton(radioFrame, text="Estudiante")
radioBtn1.grid(row=0, column=1, sticky=W)
radioBtn2 = ttk.Radiobutton(radioFrame, text="Empleado")
radioBtn2.grid(row=1, column=1, sticky=W)
radioBtn3 = ttk.Radiobutton(radioFrame, text="Desempleado")
radioBtn3.grid(row=2, column=1, sticky=W)

selectFrame = ttk.Frame(backgroundFrame, relief="raised", padding="30 10 30 10")
selectFrame.grid(row=1, column=0)
ttk.Label(selectFrame, text="Aficiones:").grid(row=0, column=0, sticky=N)
ttk.Checkbutton(selectFrame, text="Leer").grid(row=1, column=0, sticky=W)
ttk.Checkbutton(selectFrame, text="Música").grid(row=1, column=1, sticky=W)
ttk.Checkbutton(selectFrame, text="Videojuegos").grid(row=1, column=2, sticky=W)

comboFrame = ttk.Frame(backgroundFrame, padding="10 30 10 30")
comboFrame.grid(row=1, column=1)
comboEstados = ttk.Combobox(comboFrame, textvariable=estado, justify="left")
comboEstados.grid(row=0, column=0)
comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacán")

btnFrame = ttk.Frame(backgroundFrame)
btnFrame.grid(row=2, column=0,)
saveBtn = ttk.Button(btnFrame, text="Guardar")
saveBtn.grid(row=0, column=0, sticky=W)
cancelBtn = ttk.Button(btnFrame, text="Cancelar")
cancelBtn.grid(row=0, column=1, sticky=W, padx=60)

root.mainloop()
