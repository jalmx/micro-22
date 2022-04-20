from machine import ADC # importo el modulo para control y configuración de pines
from time import sleep

adc = ADC(0) # configuro el GPIO0 como ADC o entrada analógica
sleep(1) # esperamos un tiempo de estabilización

while True:
    
    value = adc.read() # esta función nos retorna el valor que existe en la entrada
    celsius = (value/1024) * 300
    fahrenheit = (value * 1.8) + 32
    
    print("Temp Celsius:", celsius, " C") # mando a la terminal la temp en Celsius
    print("Temp Fahrenheit:", fahrenheit, " F") # mando a la terminal la temp en Fahrenheit
    sleep(1) # espero un segundo