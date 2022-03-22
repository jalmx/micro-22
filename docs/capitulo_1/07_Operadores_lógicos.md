---
title: Operadores lógicos
author: Alejandro Leyva
date: 2022-03-22
---

![banner](../assets/banner.png)

# Operadores lógicos

Contamos con los operadores lógicos básicos, `AND`, `OR` y `NOT`. Los operadores lógicos toman el objeto como booleanos para realizar la comparación.

Estos operadores nos ayudan a realizar operaciones más complejas en las decisiones y ciclos.

Todo objeto con algún contenido será tomado como `True`, a menos que:

- El objetos esté vacío, como `[]`, `()`, `{}`
- El objeto es `False`
- El objeto es `0`
- El objeto es `None`
- El objeto es cadena vacía `""` o `''`

En todos estos casos, se toman como `False`.

## Operador `AND`

Con este operador se analizan dos comparaciones y `si ambas son verdaderas`, nos entrega un resultado `True`. La palabra reservada usada en python es `and`.

Tabla de verdad para el operador `and`

A|B|Resultado
:-:|:-:|:-:
False|False|False
False|True|False
True|False|False
True|True|True

La forma de aplicación:

Ejemplo|Analizando resultado |Resultado
:-|:-:|:-:
6 < 10 `and` 3 > 0 |True `and` True|True
40 < 10 `and` 13 > 5 |False `and` True|False
9 < 12 `and` 4 > 8 |True `and` False|False
6 > 10 `and` 3 < 0 |False `and` False|False

### Ejemplo con operador lógico `and`


```python
a = 10
b = 10
c = -10

if a > 0 and b > 0: 
    print("A y B son mayores que 0") 

if a > 0 and b > 0 and c > 0: 
    print("Todos los numeros son diferentes de 0") 
else: 
    print("Al menos un numero no es mayor a 0") 

```

    A y B son mayores que 0
    Al menos un numero no es mayor a 0



```python
# Aquí se comparan números, todos daran True, menos los que tenga el valor de 0
a = 10 # True
b = -12 # True
c = 0 # False
  
if a and b and e: 
    print("Todos los numeros se toman como True") 
else: 
    print("Al menos un valor es False") 
```

    Al menos un valor es False


## Operador `OR`

Con este operador se analizan dos comparaciones y si alguna es verdadera, nos entrega un resultado `True`. La palabra reservada usada en python es `or`.

Tabla de verdad para el operador `or`

A|B|Resultado
:-:|:-:|:-:
False|False|False
False|True|True
True|False|True
True|True|True

La forma de aplicación:

Ejemplo|Analizando resultado |Resultado
:-|:-:|:-:
6 < 10 `or` 3 > 0 |True `or` True|True
40 < 10 `or` 13 > 5 |False `or` True|True
9 < 12 `or` 4 > 8 |True `or` False|True
6 > 10 `or` 3 < 0 |False `or` False|False

### Ejemplo con operador lógico `or`


```python
a = 10
b = -10
c = 0
  
if a > 0 or b > 0: 
    print("A o B es mayor que 0") 
else: 
    print("A y B no son mayores a 0") 

if b > 0 or c > 0: 
    print("B o C es mayor que 0") 
else: 
    print("B y C NO no son mayores que 0") 
```

    A o B es mayor que 0
    B y C NO no son mayores que 0



```python
a = 10
b = 12
c = 0
  
if a or b or c: 
    print("Al menos un valor se considera True") 
else: 
    print("Todos los valores dan como resultado False") 
```

    Al menos un valor se considera True


## Operador `not`

Este operador invierte el resultado booleana que recibe. La palabra reservada es `not`

Tabla de verdad para el operador `not`

A|Resultado
:-:|:-:
False|True
True|False

La forma de aplicación:

Ejemplo|Analizando resultado |Resultado
:-|:-:|:-:
`not`(6 < 10) |`not`(True)|False
`not`(20 < 12) |`not`(False)|True
`not`(2 < 10) |`not`(True)|False
`not`(False)|`not`(False)|True

### Ejemplo con operador lógico `not`


```python
a = 10
  
if not a: #Invierto el valor booleano que da 10
    print("El valor booleane es True") 
    
residuo_3 = a%3
residuo_5 = a%5

print(residuo_3)
print(residuo_5)

if not ( residuo_3 == 0 or residuo_5 == 0): 
    print("10 no es divisible entre 3 o 5") 
else: 
    print("10 es divisible entre 3 or 5") 
```

    1
    0
    10 es divisible entre 3 or 5


---

Realizado por Docente: [Alejandro Leyva](https://www.alejandro-leyva.com/)

[Mecatrónica 85](https://mecatronica85.com/)

[fb/mecatronica85](https://www.facebook.com/mecatronica85)
