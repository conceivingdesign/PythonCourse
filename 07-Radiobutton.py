# Ejemplo Radiobutton

from tkinter import *
master = Tk()
v = IntVar()
Radiobutton(master, text="Opcion 1", variable=v, value=1).pack()
Radiobutton(master, text="Opcion 2", variable=v, value=2).pack()
Radiobutton(master, text="Opcion 3", variable=v, value=3).pack()
Radiobutton(master, text="Opcion 4", variable=v, value=4).pack()
mainloop()