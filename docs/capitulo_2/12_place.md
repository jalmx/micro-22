---
title: Place Manager
author: Alejandro Leyva
date: 2022-03-22
---

# Manejador `Place`

Este manejador de geometría permite ubicar widgets indicando su posición exacta (`x` e `y`) respecto a su contenedor padre.

## Sintaxis

```python
widget.place( place_options... )
```
Los argumentos que puede recibe la función `place` son:

- `anchor`: The exact spot of widget other options refer to: may be N, E, S, W, NE, NW, SE, or SW, compass directions indicating the corners and sides of widget; default is NW (the upper left corner of widget)
- `bordermode`: Modo del border del widget, por default es `INSIDE`, el otro valor puede ser `OUTSIDE`.

## Posicionamiento absoluto 

- `x`: Offset (desplazamiento) en **eje x**, en pixels.
- `y`: Offset (desplazamiento) en **eje y**, en pixels.
- `width`: Ancho del widget en pixels.
- `height`: Alto del widget en pixels.

> Todas estos valores son en pixels.

## Posicionamiento relativo

- `relx`: Offset en `horizontal` con respecto al padre, en proporción, los valores van de `0.0` (**0%**) hasta `1.0` (**100%**)
- `rely`: Offset en `vertical` con respecto al padre, en proporción, los valores van de `0.0` (**0%**) hasta `1.0` (**100%**)
- `relwidth`: Ancho del widget en proporción al padre,  los valores van de `0.0` (**0%**) hasta `1.0` (**100%**).
- `relheight`: Alto del widget en proporción al padre,  los valores van de `0.0` (**0%**) hasta `1.0` (**100%**).


## Ejemplos

```python
from tkinter import Tk, Label, Entry, Button

root = Tk()
root.title ("Mi aplicación")

L1 = Label(root, text = "Elemento 1")
L1.place(x = 0,y = 10)
E1 = Entry(root)
E1.place(x = 100,y = 10)

L2 = Label(root,text = "Elemento 2")
L2.place(x = 0,y = 50)
E2 = Entry(root)
E2.place(x = 100,y = 50)

L3 = Label(root,text = "Total")
L3.place(x = 10,y = 150)
E3 = Entry(root)
E3.place(x = 100,y = 150)

B = Button(root, text = "Agregar")
B.place(x = 150, y = 100)

root.geometry("350x250")
root.mainloop()
```

![place 1](img/place_1.png)


```python
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
```
![place 2](img/place_2.png)


## Referencias:

- https://www.tutorialspoint.com/python3/tk_place.htm
- 