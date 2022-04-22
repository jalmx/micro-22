from machine import Pin, PWM # importo el modulo para PWM y configuración de pines
from time import sleep_ms

btn_down = Pin(4,Pin.IN)
btn_up = Pin(0,Pin.IN)

motor = PWM(Pin(5)) # configuro el pin como salida PWM

value_minimum = 0 # es una referencia, porque para arrancar el motor es un valor mas alto, hacer el ajuste necesario
value = value_minimum
motor.duty(value) # apago el motor

constant = 10 # es una referencia para que vaya incrementando de 10 en 10, se puede cambiar a gusto

while True:
    
    if btn_down.value() and value > value_minimum:
        value -= constant

    if btn_up.value() and value < 1024:
        value += constant
    
    motor.duty(value) #asigno el valor de pwm 
    print(value)
    sleep_ms(150) # espero por el rebote del botón