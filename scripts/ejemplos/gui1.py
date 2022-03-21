from tkinter import *

def seleccionar():    
    if (opcion_1.get()):
        print("opción 1 marcada")
    else:
        print("opción 1 desmarcada")
        
    if (opcion_2.get()):
        print("opción 2 marcada")
    else:
        print("opción 2 desmarcada")

# Configuración de la raíz
root = Tk()
root.title("Mi aplicación")
root.config(bd=15) 

opcion_1 = IntVar()    # 1 si, 0 no
opcion_2 = IntVar()   # 1 si, 0 no

Checkbutton(root, text="Opción 1", variable=opcion_1, onvalue=1, offvalue=0, command=seleccionar).pack()

Checkbutton(root, text="Opción 2", variable=opcion_2, onvalue=1, offvalue=0, command=seleccionar).pack()

root.mainloop()