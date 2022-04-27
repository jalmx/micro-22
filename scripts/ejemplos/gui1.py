from tkinter import Tk, Checkbutton

root = Tk() # Creo mi ventana principal
root.title("Mi aplicación")
root.geometry("300x300")

Checkbutton(root, text="Opción a elegir").pack()

root.mainloop()
