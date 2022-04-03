# Secuencia de luces

from machine import ADC, Pin # importo el modulo para control y configuración de pines
from time import sleep

adc = ADC(0) # configuro el GPIO0 como ADC o entrada analógica
led_0 = Pin(16,Pin.OUT,value=0)
led_1 = Pin(5,Pin.OUT,value=0)
led_2 = Pin(4,Pin.OUT,value=0)
led_3 = Pin(0,Pin.OUT,value=0)
led_4 = Pin(2,Pin.OUT,value=0)

while True:
    valor = adc.read() # esta función nos retorna el valor que existe en la entrada
    
    if valor < 100:
        led_0.off()
        led_1.off()
        led_2.off()
        led_3.off()
        led_4.off()
    elif valor > 100 and valor <= 300:
        led_0.on()
        led_1.off()
        led_2.off()
        led_3.off()
        led_4.off()
    elif valor > 300 and valor <= 500:
        led_0.on()
        led_1.on()
        led_2.off()
        led_3.off()
        led_4.off()
        
    elif valor > 500 and valor <= 700:
        led_0.on()
        led_1.on()
        led_2.on()
        led_3.off()
        led_4.off()
        
    elif valor > 700 and valor < 950:
        led_0.on()
        led_1.on()
        led_2.on()
        led_3.on()
        led_4.off()
    else:        
        led_0.on()
        led_1.on()
        led_2.on()
        led_3.on()
        led_4.on()
        
    sleep(0.25) # espero un segundo