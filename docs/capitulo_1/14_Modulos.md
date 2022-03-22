---
title: Módulos
author: Alejandro Leyva
date: 2022-03-22
---

![banner](../assets/banner.png)

# Módulos

Son funciones que existen dentro de Python para realizar alguna cosa que necesitemos o sean comunes para resolver algún problema. Muchos módulos se deben importar, dado que no están disponible con solo invocar la función a ocupar.

## Módulo `random`

El módulo `random` genera un número al azar 0.0 <= x < 1.0. Pero tiene varias funciones que nos pueden ayudar dependiendo que vayamos a realizar.

Tienes muchas funciones útiles, pero aquí solo se mencionan algunas, para más detalles ir a la documentación oficial:

- `random()`: Retorna un número random entre 0.0 a 1.0
- `randrange(value)`: Devuelve un número entero entre 0 al valor dado menos 1.
- `choice(list):` Se le pasa una lista y retorna algún valor de ahí al azar
- `randint(min, max)`: Retorna un valor entero aleatorio entre el mínimo y máximo que se le indique

[Documentación oficial de random](https://docs.python.org/3.7/library/random.html)


```python
import random # siempre que queremos usar el modulo random lo debemos importarlo

numero_random = random.random() # esto nos regresa un numero al azar que puede ir de 0.0 a 1.0

print(numero_random)
print('----------------------------------------')
count = 0
while count < 10:
    print(random.random())
    count +=1
```

    0.9434806652958366
    ----------------------------------------
    0.9418708971399746
    0.24762891571065693
    0.9271427494593301
    0.6822774976172582
    0.23363131810814664
    0.7457655424264042
    0.4618611306880258
    0.8803150650138123
    0.7359502614366726
    0.28509275831478165



```python
#nos devuelve un valor entero de 0 al valor que le dimos - 1

numero_en_rango = random.randrange(101) 

print(numero_en_rango)
```

    27



```python
# nos devuelve un valor en el rango de 5 (min) al 15 (max)

numero_rango_min_max = random.randint(3, 15) 

print(numero_rango_min_max)
```

    8



```python
# con esta función le podemos pasar una lista y devolvera un valor de esa lista al azar

lista = ["hola","mensaje", "texto","mecatronica","cbtis85"]
valor = random.choice(lista)

print(valor)
```

    mecatronica



```python
#Juego de adivina el numero vBTV

import random

number = random.randint(1,10)

print("Juego de adivina el numero")
print("El numero esta entre 1 y 10")
print("Tienes 5 intentos")
print("Mucha suerte!!!!")

intentos = 0
while True:
    nuevo = int(input("Dame un valor: "))

    if nuevo < number:
        print("El numero es MAYOR")
        intentos +=1
    elif nuevo > number:
        print("El numero es MENOR")
        intentos +=1
    else:
        print("Felicidades le has atinado")
        break

    print(f"Llevas {intentos} intentos")
    
    if intentos == 5:
        print("Perdiste, lastima margarito  T.T")
        break
```

    Juego de adivina el numero
    El numero esta entre 1 y 10
    Tienes 5 intentos
    Mucha suerte!!!!
    Dame un valor: 5
    Felicidades le has atinado



```python
#Juego de adivina el numero vATM
import random

num_random = random.randint(1,10) #genera un numero al azar en ese rango

print("JUEGO + ADIVINA EL NUMERO")
print("El numero esta entre 1 al 10")
print("Tienes solo 5 intentos")
print("Mucha suerte >:) ")

intentos = 0
while True:
    number = int(input("Dar el numero: "))

    if number < num_random:
        print("El numero es mayor")
        intentos +=1
    elif number > num_random:
        print("El numero es menor")
        intentos +=1
    else:
        print("Felicidades le atinaste :D")
        break

    if intentos == 5:
        print(f"Fallaste {intentos} veces")
        print(f"EL numero era: {num_random}")
        print(f"Lastima margarito")
        break
```

    JUEGO + ADIVINA EL NUMERO
    El numero esta entre 1 al 10
    Tienes solo 5 intentos
    Mucha suerte >:) 
    Dar el numero: 5
    El numero es mayor
    Dar el numero: 6
    Felicidades le atinaste :D


## Módulo `math`

Este módulo es enfocado a matemáticas, tiene funciones que nos facilitan realizar cálculos complejos.

- `ceil(x)`: Retorna un entero. Redondeo hacia abajo
- `floor(x)`: Retorna un entero. Redondeo hacia arriba.
- `sqrt(x)`: Raiz cuadrada de `x`.
- `pow(base, potencia)`: es equivalente a base ** potencia = base ^ potencia
- `cos(x)`: coseno de x en radianes
- `sin(x)`: seno de x en radianes
- `tan(x)`: tangente de x en radianes
- `pi`: Devuelve el valor de PI = $\pi$ = 3.141592...
- `e`: Devuelve el valor de E (Euler) = 2.718281...


[Documentación oficial de math](https://docs.python.org/3.7/library/math.html)


```python
# Redondeos

import math

valor = 2.625

r_arriba = math.ceil(valor)
r_abajo = math.floor(valor)

print(f'Sin redondeo {valor}')
print(f'Redondeo hacia abajo {r_abajo}')
print(f'Redondeo hacia arriba {r_arriba}')
```

    Sin redondeo 2.625
    Redondeo hacia abajo 2
    Redondeo hacia arriba 3



```python
# Potencia y raíz cuadrada

potencia = math.pow(2,3) # 2^3 = 2**3
raiz = math.sqrt(25) # raiz cuadrada de 25

print(f'Elevando 2 al cubo es: {potencia}')
print(f'La raiz cuadrada de 25 es: {raiz}')
```

    Elevando 2 al cubo es: 8.0
    La raiz cuadrada de 25 es: 5.0



```python
# Funciones trigonometricas, siempre se dan los resultado en radianes, 
# si se quiere manejar grados tenemos que hacer la conversion

coseno = math.cos(45)
seno = math.sin(45)
tangente = math.tan(45)

print(f'Conseno de 30 es: {coseno}')
print(f'Seno de 30 es: {seno}')
print(f'Tangete de de 30 es: {tangente}')
```

    Conseno de 30 es: 0.5253219888177297
    Seno de 30 es: 0.8509035245341184
    Tangete de de 30 es: 1.6197751905438615



```python
# Normalmente todos los lenguajes tiene una libreria matematica y traen las constantes matematicas comunes

print(f'Valor de pi: {math.pi}')
print(f'Valor de Euler: {math.e}')
```

    Valor de pi: 3.141592653589793
    Valor de Euler: 2.718281828459045


### La función `sum`

La función `sum` es una utilidad, para realizar una *sumatoria* rápida para obtener la suma de una lista sin tener que hacerlo a mano, Python trae esta utilidad para mayor comodidad.

**Sintaxis:**

```Python
sum(list)
```

**Parámetros:**

- `list` : es una lista de números, pueden ser enteros o flotantes
- `return`: El resultado de la sumatoria de los valores de la lista


```python
# Tenemos a disposicion una función llamada sum

numeros =[1.6,2.6,3,6,7,5,85,5,87]
sumatoria = sum(numeros)

print(f'Resultado de la suma: {sumatoria}')
```

    Resultado de la suma: 202.2


### Funciones disponibles por default

Cuando iniciamos un programa en python, por default ya contamos con varias funciones disponibles para utilizarlas.

Para ver las funciones disponibles ir a la [Documentacion de python "Funciones"](https://docs.python.org/3/library/functions.html)


---

Realizado por Docente: [Alejandro Leyva](https://www.alejandro-leyva.com/)

[Mecatrónica 85](https://mecatronica85.com/)

[fb/mecatronica85](https://www.facebook.com/mecatronica85)
