from tkinter import *

root = Tk()
root.geometry("200x200")

# button widget
b2 = Button(root, text = "Botón 2 detrás del botón 1")
b2.pack(fill = X, expand = True, ipady = 10)

# button widget
b1 = Button(root, text = "Click me !")

# This is where b1 is placed inside b2 with in_ option
b1.place(in_= b2, relx = 0.5, rely = 0.5, anchor = CENTER)

# label widget
l = Label(root, text = "Etiqueta ")
l.place(anchor = NW)

mainloop()