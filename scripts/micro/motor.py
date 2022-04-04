from machine import Pin
from time import sleep
from dht import DHT11

sensor = DHT11( Pin(4) )

while True:
    sensor.measure()
    value_temperature = sensor.temperature() # se obtiene el valor de la temperatura
    value_humidity = sensor.humidity()    # se obtiene el valor de la humedad relativa
    
    print(value_temperature)
    print(value_humidity)
    
    sleep(1)