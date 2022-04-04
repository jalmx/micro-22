# MQTT

MQTT es un protocolo ligero de tipo Maquina-Maquina(`Machine-to-Machine`), lo que significa que es para comunicacion entre computadoras. El modelo de este protocolo es publicador-subscriptor (`publish-subscribe`). Usualmente corre sobre el protocolo TCP/IP, sin embargo, esta hecho para operar en conexiones de ancho de banda limitados.  [Referencia wikipedia](https://en.wikipedia.org/wiki/MQTT)


![logo](https://upload.wikimedia.org/wikipedia/commons/e/e0/Mqtt-hor.svg)

Podemos ver en la siguiente arquitectura de manera general como funciona una arquitectura MQTT básica, con un `broker` el cual gestiona todas las conexiones y envían los paquetes a su destino, y los elementos que son clientes que envían (publican) y clientes que reciben (subscriptores) los tópicos (`topics`) que desean monitorizar.

![arquitectura mqtt](https://mqtt.org/assets/img/mqtt-publish-subscribe.png)

## Conceptos claves

### Broker (`Servidor`)

### Cliente - Subscriptor (`subscriber`)

### Cliente - Publicador (`publisher`)

### Tópico (`topic`) 

Más información en [mqtt.org](https://mqtt.org)