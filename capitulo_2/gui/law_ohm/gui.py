from tkinter import *

def build_gui():
    root = Tk()
    Label(root, text="Ohm Law Calculator", font=("Hack", 20)).pack()
    
    container_options = Frame(root)
    container_options.pack()
    option_volt = Radiobutton(container_options, text="Voltaje")
    option_current = Radiobutton(container_options, text="Corriente")
    option_resistence = Radiobutton(container_options, text="Resistencia")
    
    container_input_one = Frame(root)
    label_one_line = Label(container_input_one)
    label_one_line.pack()
    input_one_line = Entry(container_input_one)
    input_one_line.pack()
    unit_one_line = Label(container_input_one)
    unit_one_line.pack()
    
    container_input_two = Frame(root)
    label_two_line = Label(container_input_two)
    label_one_line.pack()
    input_two_line = Entry(container_input_two)
    input_one_line.pack()
    unit_two_line = Label(container_input_two)
    unit_one_line.pack()
    
    btn_calculate = Button(root, text="Calculate")
    btn_calculate.pack()
    
    label_result = Label(root, text="1.0A", font=("Hack", 20) )
    label_result.pack()
    
    return root
    

def init_app():
    build_gui().mainloop()

if __name__ == "__main__":
    init_app()