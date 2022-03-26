from tkinter import *

root = Tk()
root.geometry("200x200")

etiqueta = Label(root, text="Etiqueta con un texto", background="gray")

position_x = 16 # le doy un espaciado (margen) izquierdo de 16px

position_y = 10  # le doy un espaciado (margen) superior de 10px

etiqueta.place(x=position_x, y=position_y )

boton = Button(text="Da click en el boton")

boton_width = etiqueta.winfo_reqwidth() # quiero que el boton tenga el mismo ancho que el contenido de la etiqueta
boton_position_y = position_y + etiqueta.winfo_reqheight() + 10 # sumo el alto de la etiqueta, con el margen que tiene la misma, mas 10px de separación entre la etiqueta y el boton

boton.place(x=position_x, y=boton_position_y, width=boton_width)

mainloop()
