from machine import Pin, PWM # importo el modulo para PWM y configuración de pines
from time import sleep_ms

btn_down = Pin(4,Pin.IN)
btn_up = Pin(0,Pin.IN)

pin_servo = Pin(5)
servo = PWM(pin_servo, freq=50) # configuro el pin como salida PWM

value=25 # para que se coloque en 0 grados
servo.duty(value)

while True:
    
    if btn_down.value() and value > 25:
        value -=1

    if btn_up.value() and value < 127:
        value +=1
    
    servo.duty(value) #asigno el valor de pwm 
    print(value)
    sleep_ms(250) # espero por el rebote del boton

# min = 25
# min = 127