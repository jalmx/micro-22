# import all widgets from module tkinter
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

# All importation from the module to calculate the value of resistance
from ohm_color import (
    get_value as get_value_resistance,
    get_range_tolerance,
    get_tolerance,
)

"""Data for the first combo box, band one
    """
colors_band1 = (
    "Black",
    "Brown",
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Violet",
    "Gray",
    "White",
)

"""Data for the second combo box, band two
    """
colors_band2 = (
    "Black",
    "Brown",
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Violet",
    "Gray",
    "White",
)

"""Data for the third combo box, band three
    """
multiplier_band = (
    "Black",
    "Brown",
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Violet",
    "Gray",
    "White",
    "Gold",
    "Silver",
)

"""Data for the fourth combo box, band four
    """
tolerances = ("Brown", "Red", "Green", "Blue", "Violet", "Gray", "Gold", "Silver")


def create_range_str(down=0.0, up=0.0):
    """Generate the str with format for the range of error from resistance

    Args:
        down (float, optional): Value down for range. Defaults to 0.0.
        up (float, optional): Value raise for range. Defaults to 0.0.

    Returns:
        str: String for label range
    """

    return "{0:1.4f}Ω <= R <={1:1.4f}Ω".format(down, up)


def calculate_to_ui():
    """Update all widgets in the UI"""
    print(band_1_str.get().lower())
    print(band_2_str.get().lower())
    print(band_multiplier_str.get().lower())
    print(band_tolerance_str.get().lower())

    value_ohm = get_value_resistance(
        band_1_name=band_1_str.get().lower(),
        band_2_name=band_2_str.get().lower(),
        multiplier_name=band_multiplier_str.get().lower(),
    )

    result_str.set(f"{value_ohm}Ω")

    color_tolerance = band_tolerance_str.get().lower()
    range_down, range_up = get_range_tolerance(value_ohm, color_tolerance)

    range_str.set(create_range_str(range_down, range_up))

    percentage = get_tolerance(color=color_tolerance)["percentage"]
    tolerance_str.set(f"{percentage}%")


def event_change_band(ev):
    """Function to trigger when some combo box change the value

    Args:
        ev (event): Nothing
    """
    calculate_to_ui()


def build_gui():
    """Function to build all widgets and position

    Returns:
        Tk: Return the main window
    """
    root = Tk()
    root.title("Code color Resistance")
    root.resizable(0, 0)

    Label(root, text="Code color Resistance", font=("Hack", 20, "bold")).pack(
        expand=True, fill=BOTH, padx=8, pady=8
    )

    container_bands = Frame(root)

    Label(container_bands, text="Band 1", font=("Hack", 10, "bold")).grid(
        row=0, column=0
    )

    global band_1_str
    band_1_str = StringVar()

    band_1 = Combobox(
        container_bands, values=colors_band1, state="readonly", textvariable=band_1_str
    )
    band_1.grid(row=1, column=0)
    band_1.current(1)

    band_1.bind("<<ComboboxSelected>>", event_change_band)

    Label(container_bands, text="Band 2", font=("Hack", 10, "bold")).grid(
        row=0, column=1
    )
    global band_2_str
    band_2_str = StringVar()
    band_2 = Combobox(
        container_bands, values=colors_band2, state="readonly", textvariable=band_2_str
    )
    band_2.grid(row=1, column=1)
    band_2.current(0)

    band_2.bind("<<ComboboxSelected>>", event_change_band)

    Label(container_bands, text="Band 3", font=("Hack", 10, "bold")).grid(
        row=0, column=2
    )
    global band_multiplier_str
    band_multiplier_str = StringVar()
    band_3 = Combobox(
        container_bands,
        values=multiplier_band,
        state="readonly",
        textvariable=band_multiplier_str,
    )
    band_3.grid(row=1, column=2)
    band_3.current(2)
    band_3.bind("<<ComboboxSelected>>", event_change_band)

    Label(container_bands, text="Band 4", font=("Hack", 10, "bold")).grid(
        row=0, column=3
    )
    global band_tolerance_str
    band_tolerance_str = StringVar()
    band_4 = Combobox(
        container_bands,
        values=tolerances,
        state="readonly",
        textvariable=band_tolerance_str,
    )
    band_4.grid(row=1, column=3)
    band_4.current(6)
    band_4.bind("<<ComboboxSelected>>", event_change_band)

    container_bands.pack(expand=True, fill=BOTH, padx=8, pady=8)

    container_result = Frame(root)
    Label(container_result, text="Value:", font=("Hack", 10, "bold")).pack(
        expand=True, side=LEFT
    )

    global result_str
    result_str = StringVar()

    label_result = Label(
        container_result, font=("Hack", 10, "bold"), fg="blue", textvariable=result_str
    )
    label_result.pack(side=LEFT, expand=True)

    Label(container_result, text="Tolerance:", font=("Hack", 10, "bold")).pack(
        side=LEFT, expand=True
    )

    global tolerance_str
    tolerance_str = StringVar()

    Label(
        container_result,
        textvariable=tolerance_str,
        font=("Hack", 10, "bold"),
        fg="red",
    ).pack(expand=True, side=LEFT)

    global range_str
    range_str = StringVar()

    label_range = Label(
        container_result, textvariable=range_str, font=("Hack", 10, "bold")
    )
    label_range.pack(expand=True, side=LEFT)

    container_result.pack(expand=True, fill=BOTH, padx=8, pady=8)

    img = PhotoImage(
        file="/home/xizuth/Documents/Projects/micro-22/docs/capitulo_2/GUI/code_color/assets/resistencia.png"
    )
    Label(root, image=img).pack()

    calculate_to_ui()

    return root


def init_app():
    """Function main to invoke the build gui"""
    build_gui().mainloop()


if __name__ == "__main__":
    """Function to the the app"""
    init_app()
