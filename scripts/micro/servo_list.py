from machine import Pin, PWM # importo el modulo para PWM y configuración de pines
from time import sleep

def servo_position(angule): # función para convertir el angulo al valor correspondiente de PWM
    return int(((angule * 102)/ 180) + 25)

pin_servo = Pin(5)
servo = PWM(pin_servo, freq=50) # configuro el pin como salida PWM

while True:    
    for angulo in 0,30,60,90,120,160,180:
        servo.duty(servo_position(angulo))
        print("angulo", angulo)
        sleep(1)