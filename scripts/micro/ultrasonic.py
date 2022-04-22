from time import sleep
from Ultrasonic import Ultrasonic

trigger_pin = 5
echo_pin = 4
    
sensor = Ultrasonic(trigger_pin, echo_pin)
sleep(1)

while True:
    
    print("Distance:", sensor.distance_in_cm())
    sleep(1)
    