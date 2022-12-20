#Ejercicio 12-02

from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(root, text="Manzana", variable=opcion, 
            value='Manzana', command=seleccionar).pack(anchor=W)
            

Radiobutton(root, text="Pera", variable=opcion, 
            value='Pera', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Plátano", variable=opcion,   
            value='Plátano', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Kiwi", variable=opcion,   
            value='Kiwi', command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()