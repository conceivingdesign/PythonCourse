# Ejemplo Button

from tkinter import *
master = Tk()
def pulsarBoton():
 print ("click!")
boton = Button(master, text="Pulsar", command=pulsarBoton)
boton.pack()
mainloop()