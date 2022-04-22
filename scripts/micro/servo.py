from machine import Pin, PWM # importo el modulo para PWM y configuración de pines
from time import sleep_ms

servo = PWM(Pin(5), freq=50) # configuro el pin como salida PWM

while True:
    
    # de 0 a 180
    for value in range(25,129):
        servo.duty(value)
        print(value)
        sleep_ms(100)
        
    # de 180 a 0
    for value in range(128,24,-1):
        servo.duty(value)
        print(value)
        sleep_ms(100)
        