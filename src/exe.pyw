from tkinter import *
from tkinter import ttk

root_window = Tk() #Creo la ventana principal
root_window.title("Mi ventana") #Con este método coloco el titulo de la ventana
root_window.config(bg="gray")

frm = ttk.Frame(root_window, padding=10)
frm.grid()

root_window.geometry("800x600")

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root_window.destroy).grid(column=1, row=0)

root_window.mainloop() #Para ejecutar de manera indefinida >>SIEMPRE AL FINAL<<
