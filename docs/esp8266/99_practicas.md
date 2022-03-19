# Prácticas

!!! example "Encender LEDs"
    **Descripción:** Hacer parpadear los leds, encendidos deben estar 2 segundos, y apagados un segundo, esto debe repetirse 5 veces
    **Material:** 
    - 1 Led
    - 1 R330 
    **Diagrama:** <br> ![practica 2](imgs/1.2_pract.png)


!!! example "Parpadear un led 3 veces"
    **Descripción:** Se debe lograr que parpadee un led 3 veces, en un intervalo de tiempo de medio segundo
    **Material:** 
    - 1 Led
    - 1 R330 
    **Diagrama:** <br> ![practica 2](imgs/1.2_pract.png)

!!! example "Parpadear leds de manera indefinida"
    **Descripción:** Deben quedar 2 leds parpadeando de manera indefinida, encendidos 2 segundos y apagados un segundo
    **Material:** 
    - 2 Led
    - 2 R330 
    **Diagrama:** <br> ![practica 2](imgs/1.2_pract.png)


!!! example "Semáforo de crucero"
    **Descripción:** Realizar dos semáforos en una intersección, deben trabajar de manera complementaria.
    **Material:** 
    - 6 Leds (rojo,verde y ámbar)
    - 6 R330 
    **Diagrama:** <br> ![practica 2](imgs/1.2.4_pract.png)
    **Ejemplo:**![practica 2](imgs/semaforo.jpg)


![practica 3](imgs/2.1.1_pract.png) |
| Control de 2 leds por medio de un push button; mientras se mantiene presionado el push button deben estar encendidos los leds, de lo contrario estarán apagados                                                                  

----

## Ignorar

## 4 Control de motores

- Control de un motor DC (ON-OFF)
  - Calcular la resistencia para el control del motor DC
- Motor PAP

## 5 Ciclos (while)

### LEDs

Descripción| Materiales | Diagrama pictórico 
-|-|-
5.1.1 Realizar una secuencia de leds básica, aplicando un ciclo |3 LEDs <br>3 Resistencias<br> |![ciclo_leds](imgs/secuencia.png)
**5.1.2 Simular las luces de alto en un cruce de ferrocarril, como se muestra en la imagén**|4 LEDs <br>4 Resistencias<br> |![ferrocarril](imgs/ferrocarril.gif)


### DTH11

Descripción| Materiales | Diagrama pictórico 
-|-|-
6.2.1 Leer los valores de Temperatura y humedad relativa en la terminal|1 DTH11<br>|![DTH11](imgs/dth11_1.png)
6.2.2 Leer los valores de Temperatura y humedad mostrandolo en la LCD|1 DTH11<br>1 LCD con I2C|![DTH11](imgs/dth11_lcd.png)
6.2.3 Leer los valores de Temperatura y humedad mostrandolo en la LCD, mostrar la temperatura en grados celsius y grados farenheit|1 DTH11<br>1 LCD con I2C|![DTH11](imgs/dth11_lcd.png)
6.2.4 Leer la temperatura,con forme vaya incrementando la temperatura vayán encendiendo los leds, y apagando en secuencia en función de la temperatura|1 LCD con I2C <br>3 LEDs<br>3 Resistencias|![DTH11](imgs/dth11_lcd_leds.png)

## Entras y salidas analógicas

### Entradas analógicas (ADC)

- Leer un potenciómetro y mostrarlo en terminal
- Leer LDR

## Salidas analógicas (PWM)

- Control de Led RGB
- Control de un motor DC
  - Regulador de velocidad motor DC
  - Giro de un motor DC
- Servo

## Sensores digitales

### Sensor PIR

## Sensores analógicos

## Varios

### Control de cargas de alta potencia (Relay)

### Ajustar estos ejercicios

### Sensores

#### Salidas digitales 
1. Simula un sensor de luz el cual haga encender un foco cuando incida poca luz (por debajo del 45%). En caso que supere esa cantidad de luz el foco se debe mantener apagado.
2. Simula un sensor de distancia (infrarrojo). Carrito seguido de luz. Se tendran 2 sensores infrarrojos, el derecho e izquierdo, cuando el sensor derecho detecte luz debe arrancar una llanta (motor DC izquierdo), cuando el sensor izquierdo reciba luz debe encender la llanta derecha (motor DC derecho). Cuando no reciba luz ningun sensor debe apagar ambos motores, si ambos reciben luz deben encender ambos motores.

### entrandas analogicas

1. Leer 2 potenciometros, cada uno controla una barra de leds, en el rango del 0 al 100% los leds iran encendiendo.
2. Leer un potenciometro e indicar por terminal el porcentaje equivalente, es decir, si se recibe 0.0 es equivalente al 0%, si recibes el 0.5 se imprime 50%, hasta llegar al 100%.

### sensores Analogicos

. Simular un sensor de luz junto con un sensor de presencia (digital). Dicho sensores trabajan a la par, si hay poca luz y existe presencia en el cuarto se debe encender un foco. En caso que no exista presencia sin importar la intensidad de la luz, el foco no enciende.
3. Simular un sensor infrarrojo para accionar el movimiento de un servomotor, entre mas luz incida debe incrementar el angulo del servomotor. Es decir, entre mas cerca se incrementa el angulo, entre mas lejos es menor el angulo.