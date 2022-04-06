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

!!! danger "No mezclar los manejadores"
    No se deben combinar estas manejadores dentro de un mismo contenedor. Se pueden tener diversos contenedores y en cada uno manejar un tipo distinto, si. Pero nunca dentro del mismo contenedor.

![geometry](https://s3.ap-south-1.amazonaws.com/s3.studytonight.com/tutorials/uploads/pictures/1592987369-71449.jpg)