from machine import Pin, PWM # importo el modulo para PWM y configuración de pines
from time import sleep


def servo_position(angule):
    return int(((angule * 5)/18) + 50)
    

pin_servo = Pin(5)
servo = PWM(pin_servo, freq=50) # configuro el pin como salida PWM

while True:
    
    for angulo in ( 0,30,60,90,120,160,180):
        for t in range(100):
            print("angulo", angulo)
            servo.duty(servo_position(angulo))
        