# Pines GPIO 

Los pines GPIO (Entradas y salidas de proposito general), no todos los pines se pueden usar, los que se utilizan son 0, 2, 4, 5, 12, 13, 14, 15, y 16.

Primer paso para utilizar los pines, se debe importar la librería `machine`

```python
from machine import Pin

pin = Pin(0)  #configuramos un pin y se guarda en una variable
```
o la otra manera es:

```python
import machine #importamos

pin = machine.Pin(0) #configuramos un pin y se guarda en una variable
```

Mas información en la [documentación oficial](http://docs.micropython.org/en/latest/esp8266/tutorial/pins.html)