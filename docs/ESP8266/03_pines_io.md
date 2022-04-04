# Pines GPIO Digitales

Los pines GPIO (Entradas y salidas de propósito general), no todos los pines se pueden usar, los que se utilizan son  0, 1, 2, 3, 4, 5, 12, 13, 14, 15, 16.

!!! warning "Pines de comunicación"
    Los pines `1` y `3` son de la comunicación serial `UART` (`Tx`, `Rx`); es decir, comunicación con la computadora. Si cambias su configuración pierdes comunicación por USB.

## Niveles lógicos 

Tenemos que dar las indicaciones para mandar a nivel alto las salidas del microcontrolador; es decir, mandar a un `nivel lógico 1` o `alto` o `True`, esto lo que hará será que a la salida del pin tenga un nivel de voltaje de `5V`, en caso de mandarlo a `0` o `bajo` o `False`, es equivalente a `0V`.


Programación|Nivel lógico|Digital|Voltaje
:-:|:-:|:-:|:-:
False|0|Low|0V
True|1|High|3.3V

## Relación de pines

La serigrafía que viene en la placa no coincide con los valores que podemos asignar, aquí están los valores correspondientes a  la serigrafía y el numero que debemos pasar para indicar lo que queremos controlar.

|Micropython|Físico|Consideraciones|
|:-:|:-:|-|
|**0**|`D3` | |
|**1**|`Rx` | No usar|
|**2**|`D4` | Led incorporado, enciende en `bajo`|
|**3**|Tx | No usar|
|**4**|`D2` | |
|**5**|`D1` | |
|**6**|X | No usar|
|**7**|X | No usar|
|**8**|X | No usar|
|**9**|X | No usar|
|**10**|X | No usar|
|**11**|X | No usar|
|**12**|`D6` | |
|**13**|`D7` | |
|**14**|`D5` | |
|**15**|`D8` | |
|**16**|`D0` | Tiene varias limitaciones|

Por ejemplo si colocamos el valor de 

## Control pines

Primer paso para utilizar los pines, se debe importar el modulo `machine`

```python
from machine import Pin # importamos el modulo para pines 

pin = Pin(0)  #configuramos un pin y se guarda en una variable (D3)
```
o la otra manera es:

```python
import machine #importamos el modulo machine

pin = machine.Pin(0) #configuramos un pin y se guarda en una variable (D3)
```

## Configurar I/O

Configurar pines como entrada o salida.

```python
machine.Pin(numero_pin, modo,r_pull_up, value=level)
```

- `numero_pin`: El numero del pin: 0, 2, 4, 5, 12, 13, 14, 15, y 16 
- `modo`: definir como entrada o salida
  - `Pin.IN`: Define como `entrada`
  - `Pin.OUT`: Define como `salida`
- `r_pull_up`: activar resistencia pull-up interna del microcontrolador. Solo para cuando es entrada.
- `value`: Se puede indicar al crearlo, el nivel que tendrá a la salida
  - `level`: `0` - Bajo (0V)
  - `level`: `1` - Alto (3.3V)

**Configurando entradas**

```python
import machine #importamos

pin = machine.Pin(0, machine.Pin.IN) #configuramos un pin 0 como entrada
```

Podemos activar la resistencia `PULL_UP` a la entrada

```python
import machine #importamos

pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP) #configuramos un pin 0 como entrada y su resistencia pull up
```

> *Nota:  GPIO16 no tiene el modo pull-up*

**Configurando salidas**

```python
import machine #importamos

pin = machine.Pin(0, machine.Pin.OUT) #configuramos un pin 0 como salida
```

## Escribiendo y Leyendo el Pin

**Leer el valor de entrada, solo retorno `0` o `1`**

```python
pin.value(0) 
pin.value(1)
```

**Asignar un valor a la salida, solo se puede asignar `0` o `1`**

```python
pin.off() # equivalente a pin.value(0) 
pin.on() # equivalente a pin.value(1) 
```

**Con nivel asignado al crearlo**

```python
p5 = Pin(5, Pin.OUT, value=1) # Al crearlo se le da el valor de 1 a la salida
```

## Interrupciones externas

Todos los pines pueden tener configurado la interrupción externa, excepto el GPIO16, esto se activa cuando cambia el valor de la entrada. Se asigna una `función callback` que se ejecuta en el disparo (trigger).

Primero se define el `función callback`, el cual debe recibir un argumento, debe ser el pin el cual que dispara la función:

```python
def callback(pin):
    print('pin change', pin)
```

El siguiente paso es configurar como entrada el pin:

```python
from machine import Pin
p0 = Pin(0, Pin.IN)
p2 = Pin(2, Pin.IN)
```

Por ultimo se necesita decirle a los pines cuando se dispararan, y la función que se llamara cuando este evento sea detectado:

```python
p0.irq(trigger=Pin.IRQ_FALLING, handler=callback)
p2.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback)
```
Esto indica que `p0` solo se dispara cuando sea un *flanco de bajada*; es decir, que pase la señal de un `alto` a `bajo` (*de 1 a 0*), mientras que para `p2` se activada en *flanco de bajada y de subida*; es decir, que pase de `alto` a `bajo` (*de 1 a 0*) y cambio de `bajo` a `alto` (*de 0 a 1*).

Mas información en la [documentación oficial](http://docs.micropython.org/en/latest/esp8266/tutorial/pins.html)

> *Nota: Algunas secciones son traducciones directas del sitio de Micropython, realizadas por mí*

