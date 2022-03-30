# Micropython ESP8266

En esta sección estaremos abarcando el uso de la tarjeta [ESP8266 NodeMCU](https://www.nodemcu.com/index_en.html) utilizando [Micropython](https://micropython.org).


## Mapa del sitio

<!-- Map site insert -->

<!-- Map site start -->
<!-- AUTO GENERATED -->
```markmap
# Micropython ESP8266

## [Instalación y Configuración](01_instalacion#instalacion-y-configuracion)

### [El firmware](01_instalacion#el-firmware)
### [Cargando el Firmware](01_instalacion#cargando-el-firmware)

#### [Que es el Firmware?](01_instalacion#que-es-el-firmware?)
#### [esptoo.py](01_instalacion#esptoo.py)
#### [PyFlasher](01_instalacion#pyflasher)
#### [Thonny IDE](01_instalacion#thonny-ide)
#### [Configurar Thonny para comenzar a trabajar](01_instalacion#configurar-thonny-para-comenzar-a-trabajar)

##### [Proceso de instalación](01_instalacion#proceso-de-instalacion)

## [ESP8266](02_esp8266#esp8266)

### [Especificaciones técnicas del SoC ESP8266](02_esp8266#especificaciones-tecnicas-del-soc-esp8266)
### [Pinout](02_esp8266#pinout)
### [Variantes de tarjetas Node MCU](02_esp8266#variantes-de-tarjetas-node-mcu)
### [Diagrama esquemático del Node MCU](02_esp8266#diagrama-esquematico-del-node-mcu)
### [Proceso Boot](02_esp8266#proceso-boot)

## [Pines GPIO Digitales](03_pines_io#pines-gpio-digitales)

### [Niveles lógicos](03_pines_io#niveles-logicos)
### [Relación de pines](03_pines_io#relacion-de-pines)
### [Control pines](03_pines_io#control-pines)
### [Configurar I/O](03_pines_io#configurar-i/o)
### [Escribiendo y Leyendo el Pin](03_pines_io#escribiendo-y-leyendo-el-pin)
### [Interrupciones externas](03_pines_io#interrupciones-externas)

## [Ejemplos control de entradas y salida digitales](04_practicas_io#ejemplos-control-de-entradas-y-salida-digitales)

### [Control de salidas](04_practicas_io#control-de-salidas)
### [Leyendo entradas](04_practicas_io#leyendo-entradas)
### [Display 7 segmentos](04_practicas_io#display-7-segmentos)

## [Entrada Analógica - ADC](05_entrada_adc#entrada-analogica---adc)

## [Ejercicios con ADC](06_practicas_adc#ejercicios-con-adc)

## [Salida analógica PWM](07_pwm#salida-analogica-pwm)

## [Ejercicios con PWM](08_practicas_pwm#ejercicios-con-pwm)

## [Sensores](09_sensores#sensores)

### [Variable física](09_sensores#variable-fisica)
### [Transductor](09_sensores#transductor)
### [Transductor Pasivo vs Activo](09_sensores#transductor-pasivo-vs-activo)
### [Sensores Digitales vs Analógicos](09_sensores#sensores-digitales-vs-analogicos)
### [Sensores Digitales](09_sensores#sensores-digitales)
### [Sensores Analógicos](09_sensores#sensores-analogicos)
### [Actuadores eléctricos o electrónicos](09_sensores#actuadores-electricos-o-electronicos)
### [Lista de sensores comunes](09_sensores#lista-de-sensores-comunes)

#### [Pasivos](09_sensores#pasivos)
#### [Activos](09_sensores#activos)
#### [Sensores digitales básicos vs protocolos](09_sensores#sensores-digitales-basicos-vs-protocolos)

##### [Los sensores digitales con comunicación por protocolo](09_sensores#los-sensores-digitales-con-comunicacion-por-protocolo)

## [Sensores Digitales](10_sensore_digitales#sensores-digitales)

### [Sensor PIR HC-SR501 (Sensor de presencia - Sensor Infrarrojo pasivo)](10_sensore_digitales#sensor-pir-hc-sr501-sensor-de-presencia---sensor-infrarrojo-pasivo)
### [Sensor de Temperatura y Humedad DTH11](10_sensore_digitales#sensor-de-temperatura-y-humedad-dth11)

#### [Aplicando el Sensor PIR](10_sensore_digitales#aplicando-el-sensor-pir)

## [Sensores Analógicos](11_sensores_analogicos#sensores-analogicos)

### [Sensor de Luz](11_sensores_analogicos#sensor-de-luz)
### [Sensor de Temperatura LM35](11_sensores_analogicos#sensor-de-temperatura-lm35)

## [Prácticas](99_practicas#practicas)

### [Ignorar](99_practicas#ignorar)
### [4 Control de motores](99_practicas#4-control-de-motores)
### [5 Ciclos (while)](99_practicas#5-ciclos-while)
### [Entras y salidas analógicas](99_practicas#entras-y-salidas-analogicas)
### [Salidas analógicas (PWM)](99_practicas#salidas-analogicas-pwm)
### [Sensores digitales](99_practicas#sensores-digitales)
### [Sensores analógicos](99_practicas#sensores-analogicos)
### [Varios](99_practicas#varios)

#### [LEDs](99_practicas#leds)
#### [DTH11](99_practicas#dth11)
#### [Entradas analógicas (ADC)](99_practicas#entradas-analogicas-adc)
#### [Sensor PIR](99_practicas#sensor-pir)
#### [Control de cargas de alta potencia (Relay)](99_practicas#control-de-cargas-de-alta-potencia-relay)
#### [Ajustar estos ejercicios](99_practicas#ajustar-estos-ejercicios)
#### [Sensores](99_practicas#sensores)
#### [entrandas analogicas](99_practicas#entrandas-analogicas)
#### [sensores Analogicos](99_practicas#sensores-analogicos)

##### [Salidas digitales](99_practicas#salidas-digitales)



```
<!-- Map site end -->



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
## Fuentes

Para la creación de los esquemáticos se usa [Fritzing](https://fritzing.org) y el componente del [ESP8266](https://github.com/prasertsakd/esp8266_fritzing) desde https://github.com/prasertsakd/esp8266_fritzing

![esp8266](https://raw.githubusercontent.com/prasertsakd/esp8266_fritzing/master/preview.png)