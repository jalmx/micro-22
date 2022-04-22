from mqtt import MQTTClient
from time import sleep

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


SERVER = "192.168.1.5"


c = MQTTClient(client_id="ESP8266", server="192.168.1.5")
con = c.connect()

while True:
    c.publish(b"/hola", b"esp8266")
    print("publicado")
    sleep(10)


