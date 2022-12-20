from tkinter import *
class App:
 def __init__(self, master):
     frame = Frame(master)
     label = Label(text='Esto es un ejemplo y \n hacemos un salto de linea')
     label.pack()
     frame.pack()
root = Tk()
app = App(root)
root.mainloop()