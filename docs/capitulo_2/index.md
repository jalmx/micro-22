---
title: GUI con Python
author: Alejandro Leyva
date: 2022-03-22
---

# GUI con Python - Tkinter

En esta sección estaremos viendo como realizar interfaz gráfica con Python, utilizando la librería nativa **Tkinter**.  La cual viene por default cuando instalamos el lenguaje Python.

## Mapa del sitio

<!-- Map site insert -->

<!-- Map site start -->
<!-- AUTO GENERATED -->
```markmap
# GUI con Python - Tkinter

## [Introducción a Interfaz gráfica (GUI)](01_introduccion#introduccion-a-interfaz-grafica-gui)

### [Iniciando con `Tkinter`](01_introduccion#iniciando-con-`tkinter`)
### [Tk - Ventana principal](01_introduccion#tk---ventana-principal)
### [Important Tk Concepts](01_introduccion#important-tk-concepts)
### [Widget hierarchy](01_introduccion#widget-hierarchy)
### [configuration options](01_introduccion#configuration-options)
### [geometry management](01_introduccion#geometry-management)
### [event loop](01_introduccion#event-loop)

#### [Widgets](01_introduccion#widgets)

## [Tk - Ventana principal](02_tk#tk---ventana-principal)
### [root.config(width=400, height=300)  Este sería otra manera](02_tk#root.configwidth=400,-height=300--este-seria-otra-manera)

### [Métodos relevantes de Tk](02_tk#metodos-relevantes-de-tk)

## [Frames - Marcos](03_frame#frames---marcos)

## [Etiqueta de Texto - Label](04_etiqueta#etiqueta-de-texto---label)

### [Imágenes](04_etiqueta#imagenes)

## [Botón - Button](05_boton#boton---button)

## [Entry - Entrada de texto](06_entry#entry---entrada-de-texto)

### [Funciones importantes](06_entry#funciones-importantes)

## [Text - Área de texto](07_text_area#text---area-de-texto)

### [Parámetros interesantes que podemos configurar](07_text_area#parametros-interesantes-que-podemos-configurar)

#### [Referencias](07_text_area#referencias)

## [Radio Button](08_radio#radio-button)

### [Parámetros de Radio Button](08_radio#parametros-de-radio-button)

## [Checkbutton - Botón de chequeo](09_checkbox#checkbutton---boton-de-chequeo)
## [Configuración de la raíz](09_checkbox#configuracion-de-la-raiz)

### [Parámetros de Radio Button](09_checkbox#parametros-de-radio-button)

## [Layout](10_Layout#layout)

### [Tipos de manejados de posicionamiento (geometry)](10_Layout#tipos-de-manejados-de-posicionamiento-geometry)

## [Manejador `Pack`](11_pack#manejador-`pack`)
## [Crear un Frame y se expande para tomar el tamaño de la ventana padre](11_pack#crear-un-frame-y-se-expande-para-tomar-el-tamano-de-la-ventana-padre)
## [Se crea un botón y se expande a toda la pantalla](11_pack#se-crea-un-boton-y-se-expande-a-toda-la-pantalla)
## [Se crea un botón y se expande a toda la pantalla](11_pack#se-crea-un-boton-y-se-expande-a-toda-la-pantalla)
## [Crear un Frame y se expande para tomar el tamaño de la ventana padre](11_pack#crear-un-frame-y-se-expande-para-tomar-el-tamano-de-la-ventana-padre)
## [Se crea un botón y se expande a toda la pantalla y se coloca a de izquierda a derecha](11_pack#se-crea-un-boton-y-se-expande-a-toda-la-pantalla-y-se-coloca-a-de-izquierda-a-derecha)
## [Se crea un botón y se expande a toda la pantalla y se coloca a de izquierda a derecha](11_pack#se-crea-un-boton-y-se-expande-a-toda-la-pantalla-y-se-coloca-a-de-izquierda-a-derecha)
## [Se crea un botón y se expande a toda la pantalla y se coloca a de izquierda a derecha](11_pack#se-crea-un-boton-y-se-expande-a-toda-la-pantalla-y-se-coloca-a-de-izquierda-a-derecha)
## [place widgets top down](11_pack#place-widgets-top-down)
## [place widgets side by side](11_pack#place-widgets-side-by-side)

### [Sintaxis](11_pack#sintaxis)
### [Ejemplos](11_pack#ejemplos)

## [Manejador `Place`](12_place#manejador-`place`)

### [Sintaxis](12_place#sintaxis)
### [Posicionamiento absoluto](12_place#posicionamiento-absoluto)
### [Posicionamiento relativo](12_place#posicionamiento-relativo)
### [Ejemplos](12_place#ejemplos)
### [Referencias:](12_place#referencias)

## [Manejador `Grid`](13_grid#manejador-`grid`)
## [root window](13_grid#root-window)
## [se configura el grid, cada columna con un peso distinto para que midan en proporcion, se definen 2 columnas](13_grid#se-configura-el-grid,-cada-columna-con-un-peso-distinto-para-que-midan-en-proporcion,-se-definen-2-columnas)
## [en total seria 4, es decir, el de peso de 1 tendria un 1/4 y el de 3 tendria 3/4 del espacio](13_grid#en-total-seria-4,-es-decir,-el-de-peso-de-1-tendria-un-1/4-y-el-de-3-tendria-3/4-del-espacio)
## [usuario](13_grid#usuario)
## [contraseña](13_grid#contrasena)
## [boton de iniciar sesión](13_grid#boton-de-iniciar-sesion)

### [Sintaxis](13_grid#sintaxis)
### [Ejemplos](13_grid#ejemplos)

#### [Referencias](13_grid#referencias)

## [Ventanas de Dialogo - Message box](14_dialog_box#ventanas-de-dialogo---message-box)

### [Show Info](14_dialog_box#show-info)
### [Show Warning](14_dialog_box#show-warning)
### [Show Error](14_dialog_box#show-error)
### [Ask Question](14_dialog_box#ask-question)
### [Ask Ok Cancel](14_dialog_box#ask-ok-cancel)
### [Ask Retry Cancel](14_dialog_box#ask-retry-cancel)
### [Referencias](14_dialog_box#referencias)

## [Practicas GUI](practicas#practicas-gui)

### [Convertidor de Temp](practicas#convertidor-de-temp)
### [Capacitor](practicas#capacitor)



```
<!-- Map site end -->



## Fuentes:

- https://docs.python.org/3/library/tk.html
- https://docs.python.org/3/library/tkinter.html