from tkinter import *
from tkinter import messagebox

import ohms_law

VOLT_OPTION = 0
CURRENT_OPTION = 1
RESISTANCE_OPTION = 2

menu_list = ["Voltage", "Current", "Resistance"]
unit_list = ["V", "A", "Ω"]

def change_ui():
    option = option_selected.get()
    if option == VOLT_OPTION:
        label_str_one.set(menu_list[CURRENT_OPTION])
        label_unit_one.set(unit_list[CURRENT_OPTION])
        label_str_two.set(menu_list[RESISTANCE_OPTION])
        label_unit_two.set(unit_list[RESISTANCE_OPTION])
    elif option == CURRENT_OPTION:
        label_str_one.set(menu_list[VOLT_OPTION])
        label_unit_one.set(unit_list[VOLT_OPTION])
        label_str_two.set(menu_list[RESISTANCE_OPTION])
        label_unit_two.set(unit_list[RESISTANCE_OPTION])
    elif option == RESISTANCE_OPTION:
        label_str_one.set(menu_list[VOLT_OPTION])
        label_unit_one.set(unit_list[VOLT_OPTION])
        label_str_two.set(menu_list[CURRENT_OPTION])
        label_unit_two.set(unit_list[CURRENT_OPTION])


def calculate():
    option = option_selected.get()
    value = 0.0

    value_one = value_entry_one.get()
    value_two = value_entry_two.get()

    if not len(value_one) or not len(value_two):
        messagebox.showerror("Error", "No puede haber campos vacíos")
        return

    value_one = float(value_one)
    value_two = float(value_two)

    if value_two == 0 and (option == CURRENT_OPTION or option == RESISTANCE_OPTION):
        messagebox.showerror("Error", "No puede ser cero el segundo valor, porque es infinito")
        value_label_result.set("-")
        return

    if option == VOLT_OPTION:
        value = ohms_law.voltage(value_one,value_two)
    elif option == CURRENT_OPTION:
        value = ohms_law.current(value_one,value_two)
    elif option == RESISTANCE_OPTION:
        value = ohms_law.resistance(value_one,value_two)

    value = "{0:1.4f} {1}".format(value, unit_list[option])
    value_label_result.set(value)

def build_gui():
    """Function to build de the gui of app

    Returns:
        Tk: Main windows from app
    """
    root = Tk()
    root.title("Ohm Law Calculator")
    root.resizable(0, 0)

    Label(root, text="Ohm Law Calculator", font=("Hack", 20), fg="red").pack(
        expand=True, fill=BOTH
    )

    container_options = LabelFrame(root, text="Calculate", bd=1, relief=SUNKEN)
    container_options.pack(expand=True, fill=BOTH, padx=8, pady=8, ipadx=8, ipady=8)

    global option_selected
    option_selected = IntVar()
    option_selected.set(VOLT_OPTION)

    option_volt = Radiobutton(
        container_options, text=menu_list[VOLT_OPTION], variable=option_selected, value=VOLT_OPTION, command=change_ui
    )
    option_volt.pack(side=LEFT, expand=True, fill=BOTH)
    option_volt.select()
    option_current = Radiobutton(
        container_options, text=menu_list[CURRENT_OPTION], variable=option_selected, value=CURRENT_OPTION, command=change_ui
    )
    option_current.pack(side=LEFT, expand=True, fill=BOTH)
    option_resistance = Radiobutton(
        container_options, text=menu_list[RESISTANCE_OPTION], variable=option_selected, value=RESISTANCE_OPTION, command=change_ui
    )
    option_resistance.pack(side=LEFT, expand=True, fill=BOTH)

    global label_str_one
    label_str_one= StringVar()
    label_str_one.set(menu_list[CURRENT_OPTION])
    global label_unit_one
    label_unit_one= StringVar()
    label_unit_one.set(unit_list[CURRENT_OPTION])

    global value_entry_one
    value_entry_one = StringVar()
    value_entry_one.set("0.0")

    container_input_one = Frame(root)
    container_input_one.pack(expand=True, fill=BOTH, padx=8, pady=8, ipadx=8, ipady=8)
    label_one_line = Label(container_input_one, textvariable=label_str_one)
    label_one_line.pack(side=LEFT, expand=True, fill=X)
    input_one_line = Entry(container_input_one, textvariable=value_entry_one)
    input_one_line.pack(side=LEFT, expand=True, fill=X)
    unit_one_line = Label(container_input_one, textvariable=label_unit_one)
    unit_one_line.pack(side=LEFT, ipadx=4, ipady=4)

    global label_str_two
    label_str_two= StringVar()
    label_str_two.set(menu_list[RESISTANCE_OPTION])
    global label_unit_two
    label_unit_two= StringVar()
    label_unit_two.set(unit_list[RESISTANCE_OPTION])
    global value_entry_two
    value_entry_two = StringVar()
    value_entry_two.set("0.0")
    container_input_two = Frame(root)
    container_input_two.pack(expand=True, fill=BOTH, padx=8, pady=8, ipadx=8, ipady=8)
    label_two_line = Label(container_input_two, textvariable=label_str_two)
    label_two_line.pack(side=LEFT, expand=True, fill=X)
    input_two_line = Entry(container_input_two,textvariable=value_entry_two)
    input_two_line.pack(side=LEFT, expand=True, fill=X)
    unit_two_line = Label(container_input_two, textvariable=label_unit_two)
    unit_two_line.pack(side=LEFT, ipadx=4, ipady=4)

    btn_calculate = Button(root, text="Calculate", command=calculate)
    btn_calculate.pack(expand=True, fill=X, padx=4, pady=4, ipadx=2, ipady=2)

    global value_label_result
    value_label_result=StringVar()
    value_label_result.set("-")
    label_result = Label(root, font=("Hack", 20), textvariable=value_label_result)
    label_result.pack(expand=True, fill=BOTH, pady=8)

    return root


def init_app():
    """Function to exec the app
    """
    build_gui().mainloop()


if __name__ == "__main__":
    """function main to exec the app in test
    """
    init_app()
