from machine import Pin
from time import sleep # importo la función sleep_ms

def display(number_display=tuple(), time=1):
    # segmentos del display
    Pin(5, Pin.OUT, value=number_display[0]) # segmento A - D1
    Pin(4, Pin.OUT, value=number_display[1]) # segmento B - D2
    Pin(0, Pin.OUT, value=number_display[2]) # segmento C - D3
    Pin(2, Pin.OUT, value=number_display[3]) # segmento D - D4
    Pin(14, Pin.OUT, value=number_display[4]) # segmento E - D5
    Pin(12, Pin.OUT, value=number_display[5]) # segmento F - D6
    Pin(13, Pin.OUT, value=number_display[6]) # segmento G - D7
    sleep(time) # tiempo entre cambio de numero

boton = Pin(16, Pin.IN)
number = 0

numbers = [
        #A B C D E F G
        (1,0,0,1,1,1,0), # C
        (0,0,1,1,1,1,1), # B
        (0,0,0,1,1,1,1), # T
        (0,1,1,0,0,0,0), # I
        (1,0,1,1,0,1,1), # S
        (0,0,0,0,0,0,1), # -
        (1,1,1,1,1,1,1), # 8
        (1,0,1,1,0,1,1), # 5
    ]

display(numbers[0]) # para mostrar el 0 desde el inicio
print('digito ', number)

while True:
    # creo el digito 0
    number += 1
    sleep(500)
    if number < len(numbers) :
        print('digito ', number)
        display(numbers[number])
    else:
        number=0 # reinicio el contador para que comience mostrando el cero
        display(numbers[number])
        print('digito ', number)
