from machine import Pin, ADC # importo el modulo para ADC y para el control de Pines
from time import sleep, sleep_ms

valor_disparo = 100
adc = ADC(0) # configuro el A0 como ADC o entrada analógica
valor = adc.read() # esta función nos retorna el valor que existe en la entrada
sleep(1)

led = Pin(5, Pin.OUT, value = 0) # configuro el pin para el LED y pongo en 0

while True:
    valor = adc.read() # esta función nos retorna el valor que existe en la entrada

    if valor > valor_disparo:
        led.on()
        sleep_ms(250) # doy un tiempo de estabilización
    else:
        led.off()

    sleep_ms(100) # Doy un tiempo de espera