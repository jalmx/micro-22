import machine  # importo el modulo para control y configuración de pines
from time import sleep, sleep_ms

adc = machine.ADC(0)  # configuro el GPIO0 como ADC o entrada analógica
sleep(1)  # esperamos un tiempo de estabilización

while True:
    valor = adc.read()  # esta función nos retorna el valor que existe en la entrada

    print(valor)  # mando a la terminal el valor del ADC
    sleep_ms(250)  # espero un segundo
