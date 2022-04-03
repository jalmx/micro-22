# Sensores Analógicos

Un sistema digital por default no puede leer señales analógicas, rangos u oscilaciones de voltajes. Entonces cómo se hace la medición?. Se utiliza un componente llamado **ADC (Analogue to Digital Converter)**, el cual hace la conversión de la señal analógica a un código binario, entonces en lugar de percibir un nivel de voltaje, estaremos viendo un código binario equivalente.

El ADC que trae incorporado el ESP8266 tiene una resolución de 10 bits, es decir, tiene 1024 códigos binarios que son equivalentes son:

Voltaje|Binario|Decimal|Micropython
:-:|:-:|:-:|:-:
0V|0b|0|0.0
5V|0b11 1111 1111|1023|1.0

## Sensor de Luz 

Existen varios sensores de luz, aquí estamos abarcando el mas sencillo y básico, el cual implementa una LDR (Resistencia dependiente de Luz) en una configuración de divisor de tension.

![ldr div](imgs/circuitos_ldr.png)

![sensor luz](imgs/sensor_luz.png)
<figcaption>Modulo de Sensor de luz</figcaption>

!!! example "Sensor crepuscular"
    - **Descripción:** Se debe configurar el nivel en el código para la activación del led con cierta cantidad de luz que reciba el sensor
    - **Material:** 
        - 1 LDR
        - 1 R10k
        - 1 LED
        - 1 R330
    - **Diagrama:** <br>![adc_1](imgs/ldr_led.png)
    - **Código:** 
        ```python
        from machine import Pin, ADC # importo el modulo para ADC y para el control de Pines
        from time import sleep, sleep_ms

        valor_disparo = 100
        adc = ADC(0) # configuro el A0 como ADC o entrada analógica
        valor = adc.read() # esta función nos retorna el valor que existe en la entrada
        sleep(1)

        led = Pin(5, Pin.OUT, value = 0) # configuro el pin para el LED y pongo en 0

        while True:
            valor = adc.read() # esta función nos retorna el valor que existe en la entrada

            if valor > valor_disparo:
                led.on()
                sleep_ms(250) # doy un tiempo de estabilización
            else:
                led.off()

            sleep_ms(100) # Doy un tiempo de espera
        ```

## Sensor de Temperatura LM35 

Existe una enorme variedad de sensores de temperatura, estaremos viendo el **[LM35](https://www.ti.com/lit/ds/symlink/lm35.pdf)**, sensor de temperatura lineal.

**Nos da una respuesta de 10mV/ºC**

![lm35](imgs/lm35.png)

!!! example "Termómetro"
    Vamos a realizar un termómetro con el LM35. La temperatura se mandará a la terminal. Debe mandar la temperatura en grados Celsius y grados Fahrenheit
