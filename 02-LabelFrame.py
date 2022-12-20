# LabelFrame

from tkinter import *
class App:
 def __init__(self, master):
     labelFrame = LabelFrame(master, text="Hola caracola")
     labelFrame.pack()
     self.hi_there = Button(labelFrame, text="Hola", command=self.say_hi)
     self.hi_there.pack(side=LEFT)
 def say_hi(self):
     print ("hola a todo el mundo!")
root = Tk()
app = App(root)
root.mainloop()