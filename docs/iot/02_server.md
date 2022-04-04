# Server

Se puede configurar el modulo ESP8266 como un access point, y si otros dispositivos se van a conectar con nosotros, la manera de mostrarles la actividad es creando un servidor web básico y devolviendo la respuesta en un navegador.

El siguiente código crea un servidor HTTP simple, la cual devuelve una pagina web con una tabla de los estados de todos los pines GPIO:

```python
import machine
pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]

html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
    </body>
</html>
"""

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    response = html % '\n'.join(rows)
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()
```

> No se profundizara en estos temas. Si deseas que se realicen ejemplos o detallar más usos de aplicación enviarme un correo de mi canal oficial https://www.youtube.com/c/XizuthTech o xizuth@gmail.com