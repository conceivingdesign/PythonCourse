# Ejemplo ListBox

from tkinter import *
class App:
 def __init__(self, master):
     frame = Frame(master)
     label = Label(text='Animales')
     listbox = Listbox()
     listbox.insert(0 ,('Perro'))
     listbox.insert(1, ('Gato'))
     listbox.insert(2, ('Leon'))
     listbox.insert(3, ('Pato'))
     listbox.insert(4, ('Gallina'))
     listbox.insert(5, ('Lobo'))
     label.pack()
     listbox.pack()
     frame.pack()
root = Tk()
app = App(root)
root.mainloop()