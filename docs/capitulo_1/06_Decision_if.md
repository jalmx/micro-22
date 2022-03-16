![banner](../assets/banner.png)

# Decisiones  `if` `if-else` `elif`

## ¿Qué es una estructura de decisión?

Dentro de la programación tenemos una estructura que nos ayuda a poder tomar decisiones con base a una comparación y de esta manera poder tomar un camino o tomar otro. Es una sentencias `IF`s la cual no ayuda a tomar la ruta que necesitemos


## Estructura `if`

Python la única referencia que ocupa es la **identación**, sean `espacios` o `tabs` y dos puntos `:` para indicar que comienza un bloque nuevo, en este caso una sentencia `if`.

```python
if comparacion_verdadera :
    código que ejecuta si es verdadero
    más código
    ...
```

## Operadores de comparación

Nombre | Símbolo | Ejemplo
:-|:-:|:-
Mayor que | `>` | `7 > 5 -> True`
Mayor o igual que | `>=` | `8 >= 6 -> False`
Menor que | `<` | ` 9 < 10  -> Falso`
Menor o igual que | `<=` | ` 5 <= 5 -> True`
Igual que | `==` | ` 4 == 2 -> False`
Diferente de | `!=` | ` 9 != 9 -> False`

*Nota: No puede existir espacio en el símbolo*


## Aplicando la estructura `if`

Vamos a realizar el primer ejemplo:

**1. Realizar un programa que nos diga si la edad de la persona es mayor de edad o menor de edad**

Debemos comparar la edad para saber si es mayor o no, primero verificamos si es mayor de edad, en caso de que no sea así, el programa sigue y pregunta si es menor de edad, en caso de que sea verdadero, entra y da el mensaje correspondiente.


```python
edad = 19 #Declaramos una variable donde guardaremos la edad y asignamos el valor de 18

if edad >= 18:  # recordemos que se hace una comparacion y después los dos puntos (:)
    print("Es mayor de edad")   #Recordemos que se debe aplicar una identación
    
if edad < 18:    # recordemos que se hace una comparacion y después los dos puntos (:)
    print("Es menor de edad") #Recordemos que se debe aplicar una identación
    
print("fin del programa")
```

    Es mayor de edad
    fin del programa


**2. Realizar un programa que nos diga si la edad de la persona es mayor de edad o menor de edad, la edad debe ser ingreasada desde terminal**

Debemos primero perdir la edad, una vez guardada debemos comparar la edad para saber si es mayor o no, primero verificamos si es mayor de edad, en caso de que no sea así, el programa sigue y pregunta si es menor de edad, en caso de que sea verdadero, entra y da el mensaje correspondiente.


```python
edad = input("Dar edad: ") #Pedimos el dato al usuario, este dato es tipo str
edad_int = int(edad)       #la edad esta en tipo str, lo convertimos a int para poder realizar la comparación

if edad_int >= 18:  # recordemos que se hace una comparacion y después los dos puntos (:)
    print("Eres mayor de edad")   #Recordemos que se debe aplicar una identación
    
if edad_int < 18:    # recordemos que se hace una comparacion y después los dos puntos (:)
    print("Eres menor de edad") #Recordemos que se debe aplicar una identación
```

    Dar edad: 20
    Eres mayor de edad


## Estructura `if-else`

En ocasiones necesitamos que nuestro programa tome una de las 2 rutas posibles, pero aquí en caso que no se cumpla la comparación entra al otro bloque si o si. Esta estructura es un `if-else`, *si se cumple la condición, realizo la acción, de lo contrario hago otra*

```python
if comparacion_verdadera :
    código que ejecuta si es verdadero
    más código
    ...
else:
    de lo contrario se ejecuto este código
    más código
    ...
```

Vamos a realizar el primer ejemplo:

**3. Realizar un programa que nos diga si la edad de la persona es mayor de edad o menor de edad**

*Volveremos a realizar el mismo ejemplo, pero si nos damos cuenta en este ejercicio, si no es el primer caso debe ser el segundo, no tenemos otro ruta o alguna otra decisión.*


```python
edad = int(input("Dar la edad: ")) # Tomamos el dato y directamente la conversion de str a int

if edad >= 18:  # recordemos que se hace una comparacion y después los dos puntos (:)
    print("Es mayor de edad")   #Recordemos que se debe aplicar una identación
else:           #aplicamos la palabra reservada else y sus dos puntos, esta sección siempre se ejecutará siempre que no se cumpla la condición inicial   
    print("Es menor de edad") #Recordemos que se debe aplicar una identación
```

    Dar la edad: 22
    Es mayor de edad


**4. Realizar una calculadora que pueda solo sumar y restar, dando estas opciones al usuario y realizando la opción elegida**


```python
# Damos el menu y guardamos la opcion del usuario
print("Calculadora de Suma y Resta")
print("1) Suma")
print("2) Resta")
opcion = int(input())

if opcion == 1:
    print("====== SUMA =======")
    valor_1 = int(input("Dar valor 1: " ))
    valor_2 = int(input("Dar valor 2: " ))
    suma = valor_1 + valor_2
    print("La suma es: " + str(suma))
else:
    print("====== RESTA =======")
    valor_1 = int(input("Dar valor 1: " ))
    valor_2 = int(input("Dar valor 2: " ))
    resta = valor_1 - valor_2
    print("La resta es: " + str(resta))
```

    Calculadora de Suma y Resta
    1) Suma
    2) Resta
    1
    ====== SUMA =======
    Dar valor 1: 10
    Dar valor 2: 36
    La suma es: 46


## 5 Estructura `elif`

En ocasiones necesitamos verificar varias opciones y en alguna tiene que encajar o por ultimas terminar en una opción. Para esto tenemos que combinar muchos `if` con su `else`, para ello tenemos el siguiente operador, el cual nos ayuda a hacerlo de manera corta y fácil de leer. 
Para esto siempre debemos realizar una comparación si entra en ese bloque o va al siguiente, y por ultimo si no coincide con alguna, termina en un bloque por *default*.

```python
if comparacion_verdadera :
    código que ejecuta si es verdadero
    más código
    ...
elif comparacion_verdadera:
    código que ejecuta si es verdadero
    más código
    ...
elif comparacion_verdadera:
    código que ejecuta si es verdadero
    más código
    ...
else:   #en este caso es opcional
    de lo contrario se ejecuto este código
    más código
    ...
```

**4. Realizar una calculadora que pueda solo sumar y restar, dando estas opciones al usuario y realizando la opción elegida, si da un opcion que no existe, simplemente termina el programa**

En esta ocasión si el usuario no da una opción que no existe, terminamos el programa sin indicar nada


```python
# Damos el menu y guardamos la opcion del usuario
print("Calculadora de Suma y Resta")
print("1) Suma")
print("2) Resta")
opcion = int(input())

if opcion == 1:
    print("====== SUMA =======")
    valor_1 = int(input("Dar valor 1: " ))
    valor_2 = int(input("Dar valor 2: " ))
    suma = valor_1 + valor_2
    print("La suma es: " + str(suma))
elif opcion == 2:
    print("====== RESTA =======")
    valor_1 = int(input("Dar valor 1: " ))
    valor_2 = int(input("Dar valor 2: " ))
    resta = valor_1 - valor_2
    print("La resta es: " + str(resta))
elif opcion >= 3:
    print('Saliendo del programa')
elif opcion < 0:
    print('Saliendo del programa')
    
#    Dont Repeat Yourself -> No repitas a ti mismo
```

    Calculadora de Suma y Resta
    1) Suma
    2) Resta
    -6
    Saliendo del programa


**5. Realizar una calculadora que pueda solo sumar y restar, dando estas opciones al usuario y realizando la opción elegida, si da un opcion que no existe indicar con un mensaje que la opción no existe**


```python
# Damos el menu y guardamos la opcion del usuario
print("Calculadora de Suma y Resta")
print("1) Suma")
print("2) Resta")
opcion = int(input())

if opcion == 1:
    print("====== SUMA =======")
    valor_1 = int(input("Dar valor 1: " ))
    valor_2 = int(input("Dar valor 2: " ))
    suma = valor_1 + valor_2
    print("La suma es: " + str(suma))
elif opcion == 2:
    print("====== RESTA =======")
    valor_1 = int(input("Dar valor 1: " ))
    valor_2 = int(input("Dar valor 2: " ))
    resta = valor_1 - valor_2
    print("La resta es: " + str(resta))
else:
    print("Opcion no existe")
```

    Calculadora de Suma y Resta
    1) Suma
    2) Resta
    3
    Opcion no existe


**Ejercicios:**

1. Hacer la calculadora de area y perímetro de un cuadrado, las opciones son calcular el area y el perímetro del del cuadrado, si da una opcion que no existe, indicar con un mensaje que la "opcion no existe".

## 5.5.5 Short Hands 

### 5.5.5.1 Short Hands If

Existe una versión corta cuando si la condición se cumple entra a hacer una cosa y termina.

```python
if condicion_verdadera: una_accion_a_realizar
```


```python
a = 5
b = 3

if a > b: print("a es mas grande que b")
```

    a es mas grande que b


## 5.5.6 Anidando `if`

Podemos meter `if` dentro de otro `if`, no hay limites de anidamiento. Se pueden utilizar la cantidad de `if` que sean necesarios. Esta acción se llama `ifs anidados`


```python
x = int(input(""))

if x > 10:
    print("Mayor a 10")
    if x > 20:
        print("Tambien mayor 20!")
    else:
        print("Pero menor a  20.")
```

    30
    Mayor a 10
    Tambien mayor 20!


---
Realizado por Docente: [Alejandro Leyva](https://www.alejandro-leyva.com/)

[Mecatrónica 85](https://mecatronica85.com/)

[fb/mecatronica85](https://www.facebook.com/mecatronica85)
