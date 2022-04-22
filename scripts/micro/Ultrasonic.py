from time import sleep_us
from machine import Pin,time_pulse_us
class MeasurementTimeout(Exception):
	def __init__(A,timeout):super().__init__('Measurement timeout, exceeded {} us'.format(timeout))
class Ultrasonic:
	def __init__(A,trigger_pin,echo_pin,timeout_us=30000):A.timeout=timeout_us;A.trigger=Pin(trigger_pin,mode=Pin.OUT,pull=None);A.trigger.off();A.echo=Pin(echo_pin,mode=Pin.IN,pull=None)
	def distance_in_cm(A):
		A.trigger.on();sleep_us(10);A.trigger.off();B=time_pulse_us(A.echo,1,A.timeout)
		if B<0:raise MeasurementTimeout(A.timeout)
		return B/2/29