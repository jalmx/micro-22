# Aplicación de código de colores

Vamos a realizar, solo con las funcionalidades basicas que se marcan:

Características:

- Calculo para resistencias de 4 bandas
- Debe indicar el valor ohmico correspondiente
- Indicar el valor de la tolerancia
- Debe indicar el valor que seria con su maxima y minima tolerancia

![código de colores](../imgs/app_rest.png)


## Analizando la interfaz

Vamos a marcar las secciones que tenemos en nuestra propuesta de aplicación, podemos notar las secciones con las que esta construida la aplicación, recordemos que esta imagen es solo una guía para construir de nuevo la ui. 

En esta ocasión vamos a aplicar diferente geometry managers para construir nuestra app.

![img_grid](../imgs/app_resist_grid.png)

## Estructura del proyecto

```
├── assets
│   └── resistencia.png
├── gui.py
├── __init__.py
├── main.py
└── ohm_color.py
```

## Desarrollo

### Librería o Módulo

El siguiente código realiza el calculo del valor de resistencia basándose en las bandas ya sea por el color o el numero.

```python
"""Module for calculate the value of resistance taking the number of band
"""

def get_tolerance(**value: str) -> dict:
    """Return a dict with the information about tolerance from resistace

    Returns:
        dict: all information about the tolerance: color, percentage and number
    """
    tolerances = [
        {"color": "brown", "percentage": 1, "number": 1},
        {"color": "red", "percentage": 2, "number": 2},
        {"color": "green", "percentage": 0.5, "number": 5},
        {"color": "blue", "percentage": 0.25, "number": 6},
        {"color": "violet", "percentage": 0.1, "number": 7},
        {"color": "gray", "percentage": 0.05, "number": 8},
        {"color": "gold", "percentage": 5, "number": 10},
        {"color": "silver", "percentage": 10, "number": 11},
    ]

    if value.get("color"):
        for tolerance in tolerances:
            if tolerance.get("color") == value.get("color"):
                return tolerance

    if value.get("number"):
        for tolerance in tolerances:
            if tolerance.get("number") == value.get("number"):
                return tolerance

    return None


def get_band(**value) -> dict:
    """Generate a dict with all information of color band

    Returns:
        dict: Return a dict with color, number and multiplier of color
    """
    bands = [
        {"color": "black", "number": 0, "multiplier": 1},
        {"color": "brown", "number": 1, "multiplier": 10},
        {"color": "red", "number": 2, "multiplier": 100},
        {"color": "orange", "number": 3, "multiplier": 1000},
        {"color": "yellow", "number": 4, "multiplier": 10000},
        {"color": "green", "number": 5, "multiplier": 100000},
        {"color": "blue", "number": 6, "multiplier": 1000000},
        {"color": "violet", "number": 7, "multiplier": 10000000},
        {"color": "gray", "number": 8, "multiplier": 0},
        {"color": "white", "number": 9, "multiplier": 0},
        {"color": "gold", "number": 10, "multiplier": 0.1},
        {"color": "silver", "number": 11, "multiplier": 0.01},
    ]

    if value.get("color"):
        for band in bands:
            if band.get("color") == value.get("color"):
                return band

    if value.get("number") >= 0 and value.get("number") <= 11:
        for band in bands:
            if band.get("number") == value.get("number"):
                return band

    return None


def get_value(band_1: int, band_2: int, multiplier: int) -> float:
    """Get the value of the resistance, taking the value of each band and multiplier

    Args:
        band_1 (int): Band one
        band_2 (int): Band two
        multiplier (int): Band tree or multiplier

    Returns:
        float: Value of resistance
    """
    value_1 = get_band(number=band_1)["number"]
    value_2 = get_band(number=band_2)["number"]
    multiplier = get_band(number=multiplier)["multiplier"]

    value_base = int(f"{value_1}{value_2}")

    return value_base * multiplier


def get_range_tolerance(value: float, tolerance: str):
    """Get two values of tolerance, value down and up

    Args:
        value (float): Value of resistance
        tolerance (str): name of color from tolerance

    Returns:
        tuple: first value from down, second value from up of range
    """
    value_tolerance = get_tolerance(color=tolerance)["percentage"]

    value_down = value - ((value * value_tolerance) / 100)
    value_up = value + ((value * value_tolerance) / 100)
    return (value_down, value_up)

```

### GUI

El siguiente código corresponde exclusivamente a la interfaz, sin interacción

```python
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
```

![app_gui](../imgs/app_gui_code.png)