# Request

Podemos realizar peticiones HTTP una vez conectados a una red WiFi, esto es muy util cuando necesitamos información de una API, enviar información a una base de datos, notificar a un webhook, etc.

La siguiente función realiza una petición http a una URL y lo que devuelve lo imprime por terminal.

```python
def http_get(url):
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()
```
> No se profundizara en estos temas. Si deseas que se realicen ejemplos o detallar más usos de aplicación enviarme un correo de mi canal oficial https://www.youtube.com/c/XizuthTech o xizuth@gmail.com