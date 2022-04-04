---
title: Salida analógica - PWM
---

# Salida analógica PWM

Modulación de Ancho de Pulso (`Pulse width modulation` (`PWM`)) es una manera artificial de generar una salida analógica en un pin digital. Existen dos parámetros asociados al PWM que son la ==frecuencia== y el ==ciclo de trabajo== (*duty cycle*).
El ciclo de trabajo define que tan largo sera el estado del pin en alto de `un periodo`. El máximo ciclo de trabajo es cuando el pin esta todo el tiempo en alto (100%) y el mínimo todo el tiempo en bajo (0%).

En el ESP8266 todos los pines (excepto el GPIO16 o el pin 0) soportan PWM en su salida. 

!!! warning "Limitación del PWM"
    La limitación es que todos deben correr a la misma frecuencia de trabajo, la cual esta entre 1Hz y 1kHz

![pwm signal](https://www.allaboutcircuits.com/uploads/articles/PWMDAC1_diagram1.JPG)

![pwm concepts](https://www.researchgate.net/profile/Ahmed-Elmahalawy-2/publication/271437313/figure/fig4/AS:668441367306246@1536380249520/PWM-signal-with-its-two-basic-time-periods.png)

## Aplicación de PWM

Para usar el PWM, primero se debe crear un objeto 

```python
import machine
p12 = machine.Pin(12)
```
Después, creas un objeto PWM:

```python
pwm12 = machine.PWM(p12)
```
Se puede ajustar la frecuencia y el ciclo de trabajo con:

```python
pwm12.freq(500)
pwm12.duty(512)
```

- La frecuencia va de entre `1` a `1000`, esto es equivalente a 1Hz hasta 1kHz.
- El ciclo de trabajo va de `0` a `1023`, esto es equivalente a `0%` hasta `100%`

## Referencias

http://docs.micropython.org/en/latest/esp8266/tutorial/pwm.html
