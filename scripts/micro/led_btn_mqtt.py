from mqtt import MQTTClient
from machine import Pin
from time import sleep_ms

def connect():
    import network
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('HOME-DL', 'dianalove')
        while not sta_if.isconnected():
            pass

    print('network config:', sta_if.ifconfig())
    sleep_ms(1000)

def sub_cb(topic, msg):
    print(topic, msg)

    if msg == b"0":
        led.value(0)
    elif msg == b"1":
        led.value(1)
    elif msg == b"toggle":
        led.value(not led.value())
    sleep_ms(100)


led = Pin(4, Pin.OUT)
btn = Pin(5, Pin.IN)

connect()

SERVER = "broker.hivemq.com"
PORT = 1883

c = MQTTClient(client_id="ESP8266-xlgiis6woaz", server=SERVER, port=PORT)
con = c.connect()
print("connected")

c.set_callback(sub_cb)

TOPIC_S = b"/mecatronica85/led"
c.subscribe(TOPIC_S)
print("Subscribe to",TOPIC_S)

status = 0

while True:

    if btn.value():
        led.value(not led.value())
        c.publish(b'/mecatronica85/led',str(led.value()))
        print("btn pressed")
        sleep_ms(250)

    c.check_msg() # esta funcion es igual a wait_mgs() pero es bloqueante
    sleep_ms(250)

c.disconnect()
