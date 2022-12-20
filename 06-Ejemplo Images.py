# Ejemplo Images

from tkinter import *
#crear ventana
ventana=Tk()
#título de la ventana
ventana.title("Imagenes Python")
#especificamos las dimensiones de la ventana
ventana.geometry("225x225")
#Cargar imagen
#crear variable que contiene imagen
imagen=PhotoImage(file="mundo.png")
#incluir imagen
fondo= Label(ventana,image=imagen).place(x=0,y=0)
#cerrar
ventana.mainloop()