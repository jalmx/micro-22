---
title: Ejemplos de I/O Digitales
---

# Ejemplos control de entradas y salida digitales

## Control de salidas
   
!!! example "Encender de LED básico"
    **Descripción:** Encender el led configurando un pin como salida D1
    **Material:** 
    - 1 Led
    - 1 R330 
    **Diagrama:** <br>![practica 1](imgs/1.1_pract.png)
    **Código:** 
        ```python
        
        import machine #Importo el modulo para manejo de pines

        pin = machine.Pin(5, machine.Pin.OUT) #configuro el pin D1 como salida

        pin.on() # Mando un 1 a la salida del pin 0
        ```

!!! example "Encender más LEDs"
    **Descripción:** Control de más salidas y su configuración, activar D1 y D2
    **Material:** 
    - 1 Led
    - 1 R330 
    **Diagrama:** <br> ![practica 2](imgs/1.2_pract.png)
    **Código:** 
        ```python
        
        import machine #Importo el modulo para manejo de pines

        pin1 = machine.Pin(5, machine.Pin.OUT) #configuro el pin D1 como salida
        pin2 = machine.Pin(4, machine.Pin.OUT) #configuro el pin D2 como salida
        
        pin1.value(1) # Mando un 1 a la salida del pin D1
        pin2.on() # Mando un 1 a la salida del pin D2
        ```

!!! example "Parpadear un led 3 veces"
    **Descripción:** Se debe lograr que parpadee un led 3 veces, en un intervalo de tiempo de medio segundo
    **Material:** 
    - 1 Led
    - 1 R330 
    **Diagrama:** <br> ![practica 2](imgs/1.2_pract.png)
    **Código:** 
        ```python
        import machine #Importo el modulo para manejo de pines
        import time # importa el modulo para los retardos

        time_wait = 1 # declaro una variable que usare para los retardos
        pin1 = machine.Pin(5, machine.Pin.OUT, value=0) #configuro el pin 0 como salida y lo pongo en bajo

        time.sleep(time_wait) #espero un segundo
        pin1.value(1) # Mando un 1 a la salida del pin D1
        time.sleep(time_wait) #espero un segundo
        pin1.value(0) # Mando un 0 a la salida del pin D1
        time.sleep(time_wait) #espero un segundo
        pin1.value(1) # Mando un 1 a la salida del pin D1
        time.sleep(time_wait) #espero un segundo
        pin1.value(0) # Mando un 0 a la salida del pin D1
        time.sleep(time_wait) #espero un segundo
        pin1.on() # Mando un 1 a la salida del pin D1
        time.sleep(time_wait) #espero un segundo
        pin1.off()# Mando un 0 a la salida del pin D1
        time.sleep(time_wait) #espero un segundo
        ```
!!! example "Blink"
    **Descripción:** Debe quedar parpadeando un Led por tiempo indefinido, el intervalo sera de 2 segundos.
    **Material:** 
    - 2 Leds (rojo,verde y ámbar)
    - 2 R330 
    **Diagrama:** <br> ![practica 2](imgs/1.1_pract.png)
    **Código:** 
        ```python
        import machine #Importo el modulo para manejo de pines
        import time # importa el modulo para los retardos

        time_wait = 2 # declaro una variable que usare para los retardos
        pin1 = machine.Pin(5, machine.Pin.OUT, value=0) #configuro el pin 0 como salida y lo pongo en bajo

        while True: #ciclo infinito
            
            pin1.value(1) # Mando un 1 a la salida del pin D1
            time.sleep(time_wait) #espero un segundo
            pin1.value(0) # Mando un 0 a la salida del pin D1
            time.sleep(time_wait) #espero un segundo
        ```


!!! example "Semáforo"
    **Descripción:** Se debe lograr que parpadee un led 3 veces, en un intervalo de tiempo de medio segundo
    **Material:** 
    - 3 Leds (rojo,verde y ambar)
    - 3 R330 
    **Diagrama:** <br> ![practica 2](imgs/1.2.4_pract.png)
    **Código:** 
        ```python
        ```

## Leyendo entradas

!!! example "Leyendo entrada"
    **Descripción:** Leer una entrada digital, encenderá el LED mientras se mantenga presionado el push button
    **Material:** 
    - 1 Led
    - 3 R330 
    - 1 Push button
    - 1 R1k
    **Diagrama:** <br> ![practica 2](imgs/2.1.1_pract.png)
    **Código:** 
        ```python
        from machine import Pin
        from time import sleep_ms # importo la función sleep_ms 

        pin1 = Pin(5, Pin.OUT,value=0) #configuro D1 como salida
        boton = Pin(16, Pin.IN) # configuro D0 como entrada

        while True: # ciclo infinito
                
            if boton.value(): # leo el valor del botón, si es 1 entro al bloque de código
                pin1.on() #enciendo mi led
                sleep_ms(10) #doy un tiempo mínimo para no saturar al micro
                
            pin1.off() # apago el led 
        ```

!!! example "Leyendo entrada y blick led"
    **Descripción:** Mientras se presione el botón los LEDs deben parpadear medio segundo
    **Material:** 
    - 1 Led
    - 3 R330 
    - 1 Push button
    - 1 R1k
    **Diagrama:** <br> ![practica 2](imgs/2.1.1_pract.png)
    **Código:** 
        ```python
        from machine import Pin
        from time import sleep_ms # importo la función sleep_ms 

        pin1 = Pin(5, Pin.OUT,value=0) #configuro D1 como salida
        boton = Pin(16, Pin.IN) # configuro D0 como entrada

        while True: # ciclo infinito
                
            if boton.value(): # leo el valor del botón, si es 1 entro al bloque de código
                pin1.on() #enciendo el led
                sleep_ms(500) #doy un tiempo mínimo para no saturar al micro
                pin1.off() #apago el led
                sleep_ms(500) #doy un tiempo mínimo para no saturar al micro
                
            pin1.off() # apago el led 
        ```


---

![practica 3](imgs/2.1.3_pract.png) |
| Control de 2 leds, cada uno con su propio push button, mientras sea presionado el push button debe matenerse encendido su respectivo LED                                                                                            |      2 Led<br>2 R1k<br>1 push button      | ![practica 3](imgs/2.1.4_pract.png) |
| **Toggle**: Al presionar el push button se debe encender el led y mantenerce en ese estado; hasta que se vuelva a presionar el led regresará a su estado anterior                                                                   |      2 Led<br>2 R1k<br>1 push button      | ![practica 3](imgs/2.1.1_pract.png) |
| **Toggle**: Control de 2 leds, cada uno con su propio push button, al presionar el push button se debe encender su respectivo led y mantenerce en ese estado; hasta que se vuelva a presionar el led regresará a su estado anterior |      2 Led<br>2 R1k<br>1 push button      | ![practica 3](imgs/2.1.4_pract.png) |

### Operadores lógicos

| Descripción                                                                                                                                                                                                                                                           |           Materiales            | Diagrama pictórico                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-----------------------------: | ----------------------------------- |
| Control de 2 leds, cada uno con su propio push button, mientras sea presionado el push button debe parpadear a 1/4 de segundo, encendido su respectivo LED                                                                                                            | 2 Led<br>2 R1k<br>1 push button | ![practica 3](imgs/2.1.4_pract.png) |
| Control de 2 leds, cada uno con su propio push button, mientras sea presionado el push button debe parpadear a 1/4 de segundo, encendido su respectivo LED; en caso que sean presionados ambos push button al mismo tiempo los leds van a parpadear juntos cada 200mS | 2 Led<br>2 R1k<br>1 push button | ![practica 3](imgs/2.1.4_pract.png) |

## Display de 7 segmentos

#### Display 7 segmentos

Display de 7 segmentos puede ser de ánodo o cátodo común; existen displays con mayores segmentos, hasta una matriz de puntos de diferentes resoluciones.

![display](imgs/display.png)

| Descripción                                                                                                                                                                                        | Materiales                                                                          | Diagrama pictórico                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------- |
| Creación de un contador básico con un display de 7 segmentos, el cual comenzará en 0 y terminará en F, haciendo un conteo hexadecimal, el intervalo de tiempo será de medio segundo                | 1 display de 7-segmentos, una vez que termine se reinicia automáticamente<br>7 R330 | ![practica 3](imgs/3.1.1_pract.png) |
| **Creación de un contador básico con un display de 7 segmentos, el cual comenzará en 0 y terminará en F, haciendo un conteo hexadecimal, el intercambio de digito será atraves de un push button** | 1 display de 7-segmentos<br>7 R330<br>1 push button<br>1 R1k                        | ![practica 3](imgs/3.1.1_pract.png) |
| **Crear un mensaje que se vaya leyendo en el display de 7 segmentos que diga "HOLA", el intervalor de cada letra será de medio segundo**                                                           | 1 display de 7-segmentos<br>7 R330<br>1 push button<br>1 R1k                        | ![practica 3](imgs/3.1.1_pract.png) |
| **Crear un mensaje que se vaya leyendo en el display de 7 segmentos, *tu elijes la palabra o frase*, el intervalor de cada letra será de medio segundo**                                           | 1 display de 7-segmentos<br>7 R330<br>1 push button<br>1 R1k                        | ![practica 3](imgs/3.1.1_pract.png) |
| Creación de un contador básico con un display de 7 segmentos, el cual comenzará en 0 y terminará en F, el cambio se hará cada vez que sea presionado un push button                                | 1 display de 7-segmentos<br>7 R330<br>1 push button<br>1 R1k                        | ![practica 3](imgs/3.1.4_pract.png) |
