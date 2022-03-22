---
title: Layout
author: Alejandro Leyva
date: 2022-03-22
---

# Layout

Los layout son la manera o forma de como se distribuirán los elementos en una ventana. En Python es cocido como `geometry manager`, pero aquí nos referimos como `layout` o `manejadores de posicionamiento`, por ser un nombre más común para distribución o posicionamiento de elementos (widgets) dentro de una interfaz gráfica.

## Tipos de manejados de posicionamiento (geometry)

Contamos con 3 tipos de manejadores de layout (`geometry manager`), que son:

- `pack`: Agrega los widget en bloque, uno después del otro, con forme se fueron agregando
- `place`:
- `grid`:

!!! danger "No se mezclan estos manejadores"
    No se deben combinar estas manejadores dentro de un mismo contenedor. Se pueden tener diversos contenedores y en cada uno manejar un tipo distinto, si. Pero nunca dentro del mismo contenedor.

## Manejador `Pack`

Con forme se van agregando los widget al contenedor padre, estos se irán apilando. Por default se van ordenando de arriba hacia abajo, pero se puede modificar este posición.

### Sintaxis

```python
widget.pack( pack_options... )
```

Los argumentos que puede recibe la función `pack` son:

- `side`: La posición en la que se agregará, después de ejecutar el método `pack()`
  - `TOP`: (default), Se agrega de arriaba hacia abajo
  - `BOTTOM`: Se acomoda de abajo hacia arriba
  - `LEFT`: Se acomoda de izquierda a derecha
  - `RIGHT`: Se acomoda de derecha a izquierda
- `fill`:
- `padx`/`pady`:
- `padx`/`ipady`:
- `chor`:

### Ejemplo de posicionamiento por default

```python
from tkinter import *

root = Tk()
root.title ("Normal Settings Control")

Label(root, text="Tkinter", bg="lightyellow").pack()
Label(root, text="wxPython", bg="lightgreen").pack()
Label(root, text="PyQt", bg="lightblue").pack()

root.mainloop()
```
### Ejemplo de posicionamiento custom 

```python
from Tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="green", fg="green")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()
```

https://www.youtube.com/watch?v=y69rqjEfwYI&list=PLqlQ2-9ypflQQEepQJvGQ6RJ8llnzk6Kj&index=3

https://www.tutorialspoint.com/python/tk_pack.htm

https://python-commandments.org/tkinter-pack/

https://www.pythontutorial.net/tkinter/tkinter-pack/