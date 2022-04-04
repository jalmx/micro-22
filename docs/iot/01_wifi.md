# WiFi

The network module is used to configure the WiFi connection. There are two WiFi interfaces, one for the station (when the ESP8266 connects to a router) and one for the access point (for other devices to connect to the ESP8266). Create instances of these objects using:

El modulo de red que se usa para conectar el ESP8266 es el WiFi. Hay dos interfaces, una es como estación (`station`), **cuando se conectar a un router** y el otro es como punto de acceso (`access point`), **Para que otro dispositivo se conecte a él**.

**Modo estación `station`**

![station](https://nodemcu.readthedocs.io/en/release/img/WiFi-station-mode.png)

**Modo Punto de acceso `access point`**

![access point](https://nodemcu.readthedocs.io/en/release/img/WiFi-softap-mode.png)

La forma de crear esos `objetos` es como se muestra a continuación:

```python
import network
sta_if = network.WLAN(network.STA_IF) #station
ap_if = network.WLAN(network.AP_IF) # access point
```
Se puede verificar si están activas:

```python
sta_if.active() 
```
    False


```python
ap_if.active()
```
    True

Con el siguiente método vemos la configuración:

```python
ap_if.ifconfig()
```
    ('192.168.4.1', '255.255.255.0', '192.168.4.1', '8.8.8.8')

Cuando se configura ya sea como `station` o `access point` se debe activar, con el siguiente método:

```python
sta_if.active(True)
```

Para conectar el módulo a una red WiFi
 
```python
sta_if.connect('<your ESSID>', '<your password>')
```

Para verificar si la conexión con la red esta hecha:

```python
sta_if.isconnected()
```
Una vez estamos conectados, podemos ver la IP que tenemos con el siguiente método:

```python
sta_if.ifconfig()
```
    ('192.168.0.2', '255.255.255.0', '192.168.0.1', '8.8.8.8')

Un ejemplo de función para conectar a la red de manera automática y que avise una vez la conexión este lista

```python
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<essid>', '<password>')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
``` 