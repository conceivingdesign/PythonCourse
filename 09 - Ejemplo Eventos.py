# Ejemplo Eventos

from tkinter import *
ventana=Tk()
ventana.title("Ejemplo eventos")
def mostrarDatos():
    texto1 = Label(ventana, text='Bienvenido!!! ').place(width=300,x=-130,y=20)
    texto2 = Label(ventana, text='Al curso de Python').place(width=300,x=-130,y=50)
ventana = Frame(height=200,width=250)
ventana.pack(padx=5,pady=5)
boton = Button(text="Mostrar Información",command=mostrarDatos).place(width=150, x=60,y=80)
ventana.mainloop()