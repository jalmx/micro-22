---
title: Grid Manager
author: Alejandro Leyva
date: 2022-03-22
---

# Manejador `Grid`

Este manejador de geometría es una especie de **tabla** o **rejilla** donde se irán colocando los elementos dentro del contenedor padre.

## Sintaxis

```python
widget.grid( grid_options... )
```
Los argumentos que puede recibe la función `grid` son:

- `column`: La columna donde se colocara el widget, por default es 0.
- `row`: Los renglones que ocupara el widget, por default es el primer renglón que este vació.
- `columnspan`: Cuantas columnas va a ocupar el widget, por default es 1.
- `rowspan`: La cantidad de renglones que va a ocupar el widget; por default es 1.
- `padx`/`pady`: Margen en `x` y `y`. Es la distancia entre widget y widget. Padding externo.
- `padx`/`ipady`: Padding en `x` y `y`. Es la distancia entre el contenido y la pared del widget. Padding interno.
- `sticky`: Por si necesitas que el widget abarque mas de una celda. By default, with sticky='', widget is centered in its cell. sticky may be the string concatenation of zero or more of N, E, S, W, NE, NW, SE, and SW, compass directions indicating the sides and corners of the cell to which widget sticks.
- `rowconfigure`:  con el parámetro `weight=1` indicamos que la fila se expanden o contra
- `columnconfigure`: con el parámetro `weight=1` indicamos que la columna se expanden o contra


## Ejemplos