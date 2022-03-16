![banner](../assets/banner.png)

# Estructura de repetición `for`

La siguiente estructura de control se llama `for`. Esta estructura tiene un comportamiento similar a `while`. En esencial hace lo mismo, repite hasta un limite pero este se da distinto. `For each`.

**Sintaxis:**

```python
for variable in iterador : 
    código a ejecutar
    código a ejecutar
    código a ejecutar
    ...
```

## Función `range()`

La función `range()` retorna un secuencia de números, comenzando por default en 0 e incrementando en 1, y se detiene antes del número especificado.

**Sintaxis**

```python
range(start, stop, step)
```

**Parámetros:**

- `start`	(opcional). Un numero entero específicamente para la posición inicial, por default es 0
- `stop`	(Requerido). Un numero entero que especifica en donde se detendrá.
- `step`	(opcional). Un numero entero que especifica el incremento. Por default es 1.

Esta función se utiliza con el ciclo `for`


```python
#Vamos a imprimir 10 números, del 0 al 9, recordemos que el número que le pasamos es el tope y ese no se imprime, 
#y el valor inicial por default es 0, el incremento es de 1 en 1

for valor in range(10):
    print(f'el valor actual es: "{valor}"')
    
```

    el valor actual es: "0"
    el valor actual es: "1"
    el valor actual es: "2"
    el valor actual es: "3"
    el valor actual es: "4"
    el valor actual es: "5"
    el valor actual es: "6"
    el valor actual es: "7"
    el valor actual es: "8"
    el valor actual es: "9"



```python
# Ahora vamos a imprimir en un rango, entonces se le pasa el inicio y el fin,
# comenzando en 2 y terminando en 11

for valor in range(2,12):
    print(f'el valor actual es: "{valor}"')
```

    el valor actual es: "2"
    el valor actual es: "3"
    el valor actual es: "4"
    el valor actual es: "5"
    el valor actual es: "6"
    el valor actual es: "7"
    el valor actual es: "8"
    el valor actual es: "9"
    el valor actual es: "10"
    el valor actual es: "11"



```python
# Ahora vamos a imprimir en un rango, entonces se le pasa el inicio y el fin, 
# comenzando en 1 y terminando en 20, de 2 en 2

for valor in range(3,22,2):
    print(valor)
```

    3
    5
    7
    9
    11
    13
    15
    17
    19
    21


*Nota: Cuando queramos ya sea comenzar en un numero distinto, o cero con un incremento diferente se tiene que pasar el valor de incremento forzosamente*

### Ejemplos

**1. Solicitar 3 calificaciones del parcial y calcular el promedio**


```python
suma = 0.0

for calificacion in range(3):
    suma += float(input(f"Dar el parcial {calificacion + 1}: "))

print(f"El promedio es {suma / 3}")
```

    Dar el parcial 1: 8
    Dar el parcial 2: 7
    Dar el parcial 3: 10
    El promedio es 8.333333333333334


**2. Imprimir la tabla del 7 con el formato "7 x 10 = 70"**


```python
tabla = 7

for contador in range(1,11):
    resultado = tabla * contador
    print( str(tabla) + " x " + str(contador) + " = " +  str(resultado) )

```

    7 x 1 = 7
    7 x 2 = 14
    7 x 3 = 21
    7 x 4 = 28
    7 x 5 = 35
    7 x 6 = 42
    7 x 7 = 49
    7 x 8 = 56
    7 x 9 = 63
    7 x 10 = 70



```python
for v in range(10):
    print(v)
    
    if v == 3:
        break
```

    0
    1
    2
    3



```python
mensaje = "Super mecatronica 1000%"

for letra in mensaje:
    print(letra)
```

    S
    u
    p
    e
    r
     
    m
    e
    c
    a
    t
    r
    o
    n
    i
    c
    a
     
    1
    0
    0
    0
    %



```python
#Comparativa entre el for vs while

print('Con FOR')

for contador in range(0,10):
    print(contador)
    
print('---------------')

print('Con WHILE')

contador = 0

while contador < 10:
    print(contador)
    contador += 1
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
    ---------------
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


**Ejercicio:**

1. Recorer un rango del 0 al 10 e indicar cuales son par e impar
2. Recorer un rango del 5 al 32 e indicar los que sean multiplos de 5
3. Solicitarle al usuario que tabla desea imprimir, indicando desde donde comienza y donde termina
4. Calcular el promedio de la sumatoria de los números pares desde el 2 hasta el 200

---

Realizado por Docente: [Alejandro Leyva](https://www.alejandro-leyva.com/)

[Mecatrónica 85](https://mecatronica85.com/)

[fb/mecatronica85](https://www.facebook.com/mecatronica85)
