---
title: Estructura de repetición - while
author: Alejandro Leyva
date: 2022-03-22
---

![banner](../assets/banner.png)

# Estructura de repetición `while` 

Dentro de la programación tenemos estructuras de control para repetir acciones. Hay varias estructuras que podemos utilizar, los ciclos son `while`,  `for`; este ultimo se verá en otro capítulo.

## Estructura `while`

La sintaxis de la estructura `while` es muy sencilla; es la siguiente:

```python
while condicion_verdadera:
    línea de código
    línea de código
    línea de código
    ...
```

La forma de leerla es: **mientras la condición se cumpla seguirá dentro del ciclo**.

*Lo que tiene esta estructura es que al momento de preguntar por primera vez, sino cumple la condición no entra al ciclo.*

### Ejemplo

1. **Vamos a imprimir 10 números, desde el 0 al 9, en cada vuelta del ciclo debemos tener una variable que nos ayude a saber cuando hayamos terminado.**


```python
contador = 0 # declaro mi variable auxiliar "contador"

while contador < 10:
    print(contador)     # imprimir el valor del contador
    contador = contador + 1 # incremento al contador
    
print("El ciclo termino")
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    El ciclo termino


2. **Imprimir la tabla del 7, que vaya desde el 1 al 10.**


```python
tabla = 7
contador = 1

while contador <= 10:
    print(tabla * contador)
    contador += 1
```

    7
    14
    21
    28
    35
    42
    49
    56
    63
    70


3. **solicitar al usuario 10 números e indicar si es par o impar**


```python
contador = 1

print("Par o Impar")

while contador <= 10:
    numero = int(input("Dar valor " + str(contador) + ": "))
    
    if numero % 2 == 0:
        print("El valor " + str(numero) + " es par")
    else:
        print("El valor " + str(numero) + " es impar")
    print("-------------------------------------------")

    contador +=1
```

    Par o Impar
    Dar valor 1: 51
    El valor 51 es impar
    -------------------------------------------
    Dar valor 2: 23156
    El valor 23156 es par
    -------------------------------------------
    Dar valor 3: 58616
    El valor 58616 es par
    -------------------------------------------
    Dar valor 4: 8498
    El valor 8498 es par
    -------------------------------------------
    Dar valor 5: 84198
    El valor 84198 es par
    -------------------------------------------
    Dar valor 6: 89549
    El valor 89549 es impar
    -------------------------------------------
    Dar valor 7: 9864198
    El valor 9864198 es par
    -------------------------------------------
    Dar valor 8: 8964
    El valor 8964 es par
    -------------------------------------------
    Dar valor 9: 984
    El valor 984 es par
    -------------------------------------------
    Dar valor 10: 89498
    El valor 89498 es par
    -------------------------------------------


4. **Solicitar las 3 calificaciones de materia e imprimir su promedio con la frase de "Aprobo" o "Reprobo" dependiendo el caso**


```python
print("Calculadora de promedio final")

suma = 0 # guarda la suma de los parciales
calificaciones = 1 # variable que lleva el coteo

while calificaciones <= 3:
    calificacion = int( input("Dar calificacion " + str(calificaciones) + ": ") )
    suma += calificacion
    calificaciones += 1
    
promedio = suma / 3

if(promedio < 6 ):
    print("No has aprobado, tu promedio es " + str(promedio))
else:
    print("Has aprobado, tu promedio es " + str(promedio))
```

    Calculadora de promedio final
    Dar calificacion 1: 5
    Dar calificacion 2: 8
    Dar calificacion 3: 10
    Has aprobado, tu promedio es 7.666666666666667


5. **Realizar una calculadora para sumar y restar, pero hasta que el usuario de la opcion de salir el programa terminará**


```python
opcion = 0

while opcion != 3:    
    print("-------------------------------------")
    print("Calculadora Suma y Resta")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir")
    opcion = int(input())

    if opcion == 1:
        valor1 = float(input("Dar el primer valor"))
        valor2 = float(input("Dar el segundo valor"))
        print("La suma es: " + str(valor1 + valor2))
    if opcion == 2:
        valor1 = float(input("Dar el primer valor"))
        valor2 = float(input("Dar el segundo valor"))
        print("La resta es: " + str(valor1 - valor2))
    if opcion > 3 or opcion < 1:
        print("La opcion no existe")

print("Programa a finalizado")   
```

    -------------------------------------
    Calculadora Suma y Resta
    1. Suma
    2. Resta
    3. Salir
    1
    Dar el primer valor2
    Dar el segundo valor6
    La suma es: 8.0
    -------------------------------------
    Calculadora Suma y Resta
    1. Suma
    2. Resta
    3. Salir
    2
    Dar el primer valor85
    Dar el segundo valor36
    La resta es: 49.0
    -------------------------------------
    Calculadora Suma y Resta
    1. Suma
    2. Resta
    3. Salir
    5
    La opcion no existe
    -------------------------------------
    Calculadora Suma y Resta
    1. Suma
    2. Resta
    3. Salir
    -58
    La opcion no existe
    -------------------------------------
    Calculadora Suma y Resta
    1. Suma
    2. Resta
    3. Salir
    3
    Programa a finalizado


### Ejercicios:

1. Imprimir la tabla del 8, del 1 al 10, con el siguiente formato "8 x 1 = 8"
2. Realizar un programa que solicite 10 números e imprima si es par o impar y si es mayor a 10 que lo indique, de lo contrario solo dice "es impar"
3. Realizar un programa solicite los 3 parciales de Matemáticas, e imprimir el promedio, pero si reprueba, ahora á que pedir el resultado de su extra, en caso que haya pasado el extra, le dará su calificacion final y le dirá "aprobado". En caso que no apruebe su extra, solo le dirá "estas en recursamiento"

## Continue y Break

Existen 2 palabras reservadas que nos ayudan a un control mas complejo dentro de los ciclos, que son `break` y `continue`.

- La palabra reservada `break` me sirve para romper un ciclo cuando yo no necesite, muy util en ciclos infinitos que necesitemos `romper`.
- La palabra reservada `continue` me sirve para ignorar el codigo restante e iniciar la siguiente vuelta del ciclo.



```python
# Vamos a hacer un ciclo infinito el cual vamos a romper cuando una condicion se cumpla

contador = 0

while True: # ciclo infinito
    print('El valor del contador es: ' + str(contador))
    contador+=1
   
    if contador == 5: # en el momento que esta condición se cumple entra y encuentra break
        print("Se rompe el ciclo en el valor " + str(contador))
        break   # cuando se ejecute esta linea el ciclo termina        
```

    El valor del contador es: 0
    El valor del contador es: 1
    El valor del contador es: 2
    El valor del contador es: 3
    El valor del contador es: 4
    Se rompe el ciclo en el valor 5



```python
# vamos a hacer que el ciclo ignore todo el código que tiene por debajo cuando encuentre la palabra continue

contador = 0

while contador < 5:
    contador+=1
    
    if contador == 3:
        continue
    print(f"El valor del contador es: {contador}")
    
```

    El valor del contador es: 1
    El valor del contador es: 2
    El valor del contador es: 4
    El valor del contador es: 5



```python
# Realizar una calculadora que sume y reste, mostrando un menu indicando las opciones,
# Debe tener la opcion de salir, en caso que ingrese una opcion que no existe,
# mandar el mensaje de que la opcion no es valida. El programa termina cuando el usuario
# ingresa la opcion de salir, de lo contrario debe seguir mostrando el menu con las opciones
while True:    
    print("-------------------------------------")
    print("Calculadora Suma y Resta")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir")
    opcion = int(input())

    if opcion == 1:
        valor1 = float(input("Dar el primer valor"))
        valor2 = float(input("Dar el segundo valor"))
        suma = valor1 + valo2
        print("La suma es: " + str(suma))
    elif opcion == 2:
        valor1 = float(input("Dar el primer valor"))
        valor2 = float(input("Dar el segundo valor"))
        print("La resta es: " + str(valor1 - valor2))
    elif opcion == 3:
        print("Programa a finalizado")
        break
    else:
        print("La opcion no existe")
```

    -------------------------------------
    Calculadora Suma y Resta
    1. Suma
    2. Resta
    3. Salir
    2
    Dar el primer valor36
    Dar el segundo valor36
    La resta es: 0.0
    -------------------------------------
    Calculadora Suma y Resta
    1. Suma
    2. Resta
    3. Salir
    5
    La opcion no existe
    -------------------------------------
    Calculadora Suma y Resta
    1. Suma
    2. Resta
    3. Salir
    -6
    La opcion no existe
    -------------------------------------
    Calculadora Suma y Resta
    1. Suma
    2. Resta
    3. Salir
    3
    Programa a finalizado

---

Realizado por Docente: [Alejandro Leyva](https://www.alejandro-leyva.com/)

[Mecatrónica 85](https://mecatronica85.com/)

[fb/mecatronica85](https://www.facebook.com/mecatronica85)
