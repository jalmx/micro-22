from mqtt import MQTTClient
from machine import Pin
from time import sleep_ms, sleep

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
    sleep(1)

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

connect()

SERVER = "192.168.1.5"

c = MQTTClient(client_id="ESP8266", server="192.168.1.5")
con = c.connect()
print("connected")

c.set_callback(sub_cb)

TOPIC = b"/led"
c.subscribe(TOPIC)
print("Subscribe to",TOPIC)

status = 0

while True:
    c.wait_msg()
    sleep(1)

c.disconnect()
