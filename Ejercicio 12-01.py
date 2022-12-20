## Ejercicio 12-01

from tkinter import *
master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ["Cero", "Uno", "Dos", "Tres", "Cuatro"]:
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Números")
label.pack()
master.mainloop()