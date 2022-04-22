from machine import Pin, ADC, PWM  # importo el modulo para PWM y configuración de pines
from time import sleep_ms

motor = PWM(Pin(5))  # configuro el pin como salida PWM
adc = ADC(0)

value = adc.read()

while True:
    value = adc.read()
    servo.duty(value)
    sleep_ms(100)
