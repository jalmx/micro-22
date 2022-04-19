from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox # import all widgets from module tkinter

def build_gui():
    """Function to build all widgets and position

    Returns:
        Tk: Return the main window
    """    
    root = Tk()
    root.title("Code color Resistance")
    root.resizable(0,0)
    
    Label(root, text="Code color Resistance", font=("Hack", 20)).pack(expand=True, fill=BOTH, padx=8, pady=8)
    
    container_bands = Frame(root)
    Label(container_bands, text="Band 1").grid(row=0, column=0)
    band_1 = Combobox(container_bands, values=("Cafe","Rojo"), state="readonly",textvariable="hola").grid(row=1, column=0)
    Label(container_bands, text="Band 2").grid(row=0, column=1)
    band_2 = Combobox(container_bands, values=("Naranja","Morado"), state="readonly",textvariable="hola").grid(row=1, column=1)
    Label(container_bands, text="Band 3").grid(row=0, column=2)
    band_3 = Combobox(container_bands, values=("Azul","Amarillo"), state="readonly",textvariable="hola").grid(row=1, column=2)
    Label(container_bands, text="Band 4").grid(row=0, column=3)
    band_4 = Combobox(container_bands, values=("Blanco","Gris"), state="readonly",textvariable="hola").grid(row=1, column=3)
        
    container_bands.pack(expand=True, fill=BOTH,padx=8, pady=8)
    
    container_result = Frame(root)
    Label(container_result, text="Value:").pack(expand=True, side=LEFT)
    label_result = Label(container_result, text="10 ohms")
    label_result.pack(side=LEFT, expand=True)
    
    Label(container_result, text="Tolerance:").pack(side=LEFT, expand=True)
    label_tolerance = Label(container_result, text="10%")
    label_tolerance.pack(expand=True, side=LEFT)
    
    label_range = Label(container_result, text="11 <= R <= 20")
    label_range.pack(expand=True, side=LEFT)
    
    container_result.pack(expand=True, fill=BOTH, padx=8, pady=8)
    
    img = PhotoImage(file="/home/xizuth/Documents/Projects/micro-22/docs/capitulo_2/GUI/code_color/assets/resistencia.png")
    Label(root, image=img).pack( )
       
    return root
    

def init_app():
    """Function main to invoke the build gui
    """
    build_gui().mainloop()    

if __name__ == "__main__":
    """Function to the the app
    """    
    init_app()

# https://www.pythontutorial.net/tkinter/tkinter-combobox/