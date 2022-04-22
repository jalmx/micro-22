# MQTT

MQTT es un protocolo ligero de tipo Maquina-Maquina(`Machine-to-Machine`), lo que significa que es para comunicación entre computadoras. El modelo de este protocolo es publicador-subscriptor (`publish-subscribe`). Usualmente corre sobre el protocolo TCP/IP, sin embargo, esta hecho para operar en conexiones de ancho de banda limitados.  [Referencia wikipedia](https://en.wikipedia.org/wiki/MQTT)


![logo](https://upload.wikimedia.org/wikipedia/commons/e/e0/Mqtt-hor.svg)

Podemos ver en la siguiente arquitectura de manera general como funciona una arquitectura MQTT básica, con un `broker` el cual gestiona todas las conexiones y envían los paquetes a su destino, y los elementos que son clientes que envían (publican) y clientes que reciben (subscriptores) los tópicos (`topics`) que desean monitorizar.

![arquitectura mqtt](https://mqtt.org/assets/img/mqtt-publish-subscribe.png)

## Conceptos claves

Estos conceptos son vitales para comprende los nombres de cada elemento y cual es su función.

### Broker (`Servidor`)

El broker es equivalente al servidor, el cual gestiona todas las conexiones de los clientes, `subscriptores` y `publicadores`, es decir, se conectan a él; el `broker` conoce a todos los clientes y sabra que `publicador` manda qué dato para redireccionarlo al `subscriptor` o `subscriptores` correspondientes.

### Cliente - Subscriptor (`subscriber`)

Es el cliente que quiera recibir el `mensaje` del algún `publicador` por medio de un `topic`.

### Cliente - Publicador (`publisher`)

Es el cliente que manda un `mensaje` a traves de algún `topic`.

### Tópico (`topic`)

El tópico es el nombre que se le da a la ruta por la cual se enviá o recibe un dato. Es decir, el publicador enviá su dato a traves de esa ruta (topic) y los `subscriptores` que estén registrados en ese `topic` recibirán la información.

> Nota: Un mismo dispositivo puede ser `publisher` y `subscriber` y pueden estar recibiendo y enviando en diferentes `topics`.

![arquitectura](https://www.netburner.com/wp-content/uploads/2019/02/MQTT.png)

![arquitectura](https://res.cloudinary.com/practicaldev/image/fetch/s--_bDINNUR--/c_limit,f_auto,fl_progressive,q_auto,w_880/https://bugfender.com/wp-content/uploads/2020/06/MQTT_1.png)

> [Guía completa de MQTT](https://www.hivemq.com/mqtt-essentials/)

## Brokers públicos

A traves de internet hay varios `brokers` gratuitos con fines educativos y de prueba, no se recomiendan para uso en producción, o para transferencia de información sensible.


## Lista de brokers

Documentación de [MQTT en mosquitto](https://mosquitto.org/man/mqtt-7.html)

Por default se sabe que los puertos 1883 son `sin encriptación`, puertos 8883 `encriptado` (SSL).

### Project Eclipse

#### mqtt.eclipseprojects.io

This is a public test MQTT broker service. It currently listens on the following ports:

1883 : MQTT over unencrypted TCP
8883 : MQTT over encrypted TCP
80 : MQTT over unencrypted WebSockets (note: URL must be /mqtt )
443 : MQTT over encrypted WebSockets (note: URL must be /mqtt )

- mqtt.eclipseprojects.io:1883
- mqtt.eclipseprojects.io:8883

Información de [eclipseprojects](http://mqtt.eclipseprojects.io)

### HiveMQ

- Broker http://www.mqtt-dashboard.com/
- Client dashboard http://www.hivemq.com/demos/websocket-client/
- broker.hivemq.com
  - mqtt: 1883
  - ws: 8000

### [Shiftr.io](https://shiftr.io/)

- broker.shiftr.io:1883 (mqtt)
- broker.shiftr.io:8883 (mqtts)
- broker.shiftr.io:80 (websocket)
- broker.shiftr.io:443 (websocket secure)

### Mosquitto

This is test.mosquitto.org. It hosts a publicly available Eclipse Mosquitto MQTT server/broker. MQTT is a very lightweight protocol that uses a publish/subscribe model. This makes it suitable for "machine to machine" messaging such as with low power sensors or mobile devices.

For more information on MQTT, see http://mqtt.org/ or the Mosquitto MQTT man page.

The server
The server listens on the following ports:

- `1883` : MQTT, unencrypted, unauthenticated
- `1884` : MQTT, unencrypted, authenticated
- `8883` : MQTT, encrypted, unauthenticated
- `8884` : MQTT, encrypted, client certificate required
- `8885` : MQTT, encrypted, authenticated
- `8886` : MQTT, encrypted, unauthenticated
- `8887` : MQTT, encrypted, server certificate deliberately expired
- `8080` : MQTT over WebSockets, unencrypted, unauthenticated
- `8081` : MQTT over WebSockets, encrypted, unauthenticated
- `8090` : MQTT over WebSockets, unencrypted, authenticated
- `8091` : MQTT over WebSockets, encrypted, authenticated

[Ir a su web](http://test.mosquitto.org)


**Mejores prácticas para topics** https://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices/

## Others Brokers

- [ioticos](https://ioticos.org/)
- [flespi](https://flespi.com/mqtt-broker)
- [dioty](http://www.dioty.co/)
- [iotwithus](https://www.iotwithus.com/free-mqtt-server/)
- [mqtt.su](https://www.mqtt.su/index.php)
- [List brokers](https://github.com/mqtt/mqtt.github.io/wiki/public_brokers)

[Fuente](https://mqtt.org/software/)

Más información en [mqtt.org](https://mqtt.org)

## Clientes

Existen diversas aplicaciones para poder realizar el monitoreo de los dispositivos IoT a traves del protocolo MQTT, se pueden ocupar cualquiera, pero aquí vamos a utilizar cualquiera de las siguientes

[MQTT Explorer](https://mqtt-explorer.com)

![mqtt explorer](https://mqtt-explorer.com/img/screen-composite.png)

[MQTT X](https://mqttx.app)

![mqtt x](https://raw.githubusercontent.com/emqx/MQTTX/main/assets/mqttx-preview.png)

**Extension de Chrome**

[MQTT Box](https://chrome.google.com/webstore/detail/mqttbox/kaajoficamnjijhkeomgfljpicifbkaf)

![imgs/mqttbox.jpg](imgs/mqttbox.jpg)

**Cliente Dashboard IoT**

> Hecho por [Alejando Leyva](https://github.com/jalmx/dashboard-iot)

[Ir al cliente](http://www.alejandro-leyva.com/dashboard-iot/)

[![dashboard](https://raw.githubusercontent.com/jalmx/dashboard-iot/master/imgs/screencapture-1.png)](http://www.alejandro-leyva.com/dashboard-iot/)
