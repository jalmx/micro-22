from dht import DHT11
from machine import Pin
from time import sleep

sensor = DHT11( Pin(5) )

while True:
    sensor.measure()
    celsius = sensor.temperature() # se obtiene el valor de la temperatura
    fahrenheit = (celsius * 1.8) + 32
    
    print("Temp Celsius:", celsius, " C") # mando a la terminal la temp en Celsius
    print("Temp Fahrenheit:", fahrenheit, " F") # mando a la terminal la temp en Fahrenheit
    
    sleep(1) #esperamos 1 seg para la siguiente lectura de las variables ambientales