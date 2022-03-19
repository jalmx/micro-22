# Micropython ESP8266

En esta sección estaremos abarcando el uso de la tarjeta [ESP8266 NodeMCU](https://www.nodemcu.com/index_en.html) utilizando [Micropython](https://micropython.org).


## Mapa de esta sección

## Módulos de Micropython vs Python3

### Temporizadores y Relojes

Para utilizar temporizadores se tiene el modulo `time`:

```python
import time

time.sleep(1)           # sleep for 1 second
time.sleep_ms(500)      # sleep for 500 milliseconds
time.sleep_us(10)       # sleep for 10 microseconds
start = time.ticks_ms() # get millisecond counter
delta = time.ticks_diff(time.ticks_ms(), start) # compute time difference
```

El temporizador tiempo un limite, el cual es de 7:41 horas, después de esto el reloj se desborda, es decir, se reinicia.

### Relojes (Timers)

Son relojes virtuales basado en RTO. Se usa la clase `machine.Timer`, indicando su ID de `-1`. El periodo es en `milisegundos`.

```python
from machine import Timer

tim = Timer(-1)
tim.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
tim.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))
```

