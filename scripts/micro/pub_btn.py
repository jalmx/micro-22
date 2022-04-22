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


btn = Pin(5, Pin.IN)

connect()

SERVER = "192.168.1.5"

c = MQTTClient(client_id="ESP8266", server=SERVER)
con = c.connect()
print("connected")

while True:

    if btn.value():
        c.publish(b"/btn", b"{\"btn\":\"on\"}")
        print("btn presionado")
        sleep_ms(250)






