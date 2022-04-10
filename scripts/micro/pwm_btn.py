from machine import Pin, PWM # importo el modulo para PWM y configuración de pines
from time import sleep_ms

led_r = Pin(5) #Creo el pin 
led_g = Pin(4) #Creo el pin 
led_b = Pin(0) #Creo el pin 
red = PWM(led_r) # configuro el pin como salida PWM
green = PWM(led_g) # configuro el pin como salida PWM
blue = PWM(led_b) # configuro el pin como salida PWM

btn_r = Pin(14, Pin.IN)
btn_g = Pin(12, Pin.IN)
btn_b = Pin(13, Pin.IN)

value_r = 0
value_g = 0
value_b = 0

while True:
    
    if btn_r.value():
        if value_r >= 1024:
            value_r = 0
            red.duty(value_r)
            
        elif value_r < 1025:
            value_r += 8
            red.duty(value_r) # cargo el valor de 0 a 1023
        
    
    if btn_g.value() :
        if value_g >= 1024:
            value_g = 0
            green.duty(value_g)
        elif value_g < 1025:
            value_g += 8
            green.duty(value_g) # cargo el valor de 0 a 1023
            
    if btn_b.value():
        if value_b >= 1024:
            value_b = 0
            blue.duty(value_b)
        elif value_b < 1025:
            value_b += 8
            blue.duty(value_b) # cargo el valor de 0 a 1023
        
    
    print(value_r,value_b,value_g)
    sleep_ms(250) # espero medio segundo