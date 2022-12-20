# Ejemplo Checkbutton
from tkinter import *

top = Tk()
titulo= Label(text="¿Que lenguaje de programación te gusta más?")
titulo.pack()
opcion1 = IntVar()
opcion2 = IntVar()
opcion3 = IntVar()
top.title("Ejemplo Checkbutton")

Op1 = Checkbutton(top, text = "Java", variable = opcion1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
Op2 = Checkbutton(top, text = "Python", variable = opcion2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
Op3 = Checkbutton(top, text = "Javascript", variable = opcion3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
Op1.pack()
Op2.pack()
Op3.pack()
top.mainloop()