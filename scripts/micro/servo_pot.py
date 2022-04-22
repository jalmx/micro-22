from machine import Pin,ADC, PWM # importo el modulo para PWM y configuración de pines
from time import sleep_ms

def maps(x, min_in, max_in, min_out,max_out): # inspirada de https://www.arduino.cc/reference/en/language/functions/math/map/
    """_summary_

    Args:
        x (number): The value to change range
        min_in (number): Minimum value input
        max_in (number): Maximum value input
        min_out (number): Minimum value output
        max_out (number): Maximum value output

    Returns:
        int: Value mapped
    """    
    return int(( x - min_in) * (max_out - min_out) / (max_in - min_in) + min_in)

def servo_position(angule): # función para convertir el angulo al valor correspondiente de PWM
    return int(((angule * 102)/ 180) + 25)

servo = PWM(Pin(5), freq=50) # configuro el pin como salida PWM
adc = ADC(0)

value = adc.read()

while True:
    value = adc.read()
    angule = maps(value, 0, 1024, 0, 180)
    duty = servo_position(angule)
    servo.duty(duty)
    print("angule",angule)
    sleep_ms(250)
    