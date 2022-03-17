![banner](../assets/banner.png)

# Colecciones

Dentro de los lenguajes de programación hay tipos datos que son estructuras que pueden contener más de un dato, a comparación de los tipos de datos básicos, estas estructuras pueden contener muchos de esos datos básicos en su interior. Podrías decir que es una base de datos, pero esta solo existe mientras está la aplicación en ejecución, los datos son temporales. Las colecciones pueden contener cualquier tipo de dato, incluso mas colecciones.

En python son los siguientes:

- `Tuplas` Tipo de dato Inmutable
- `Listas (arrays)` Tipo de Mutable
- `Diccionarios`
- `Sets`

*Nota: En este curso solo se cubrirán las tuplas y las listas.*

## Tuplas

Es una estructura de datos **inmutables**, una vez declarada no puede cambiar su contenido, ni agregar, ni eliminar, no modificar. 

Cada posición de los datos tiene un **indice** (index), el cual me ayuda a acceder a el. *La primera posición siempre es 0*.

**La convención de como declarar o nombrar a una lista o tupla es en plural**

Parámetros a destacar:

- index: Indice
- len: Longitud

**Sintaxis:**

```python
nombre_tupla = (dato1, dato2, ..., datoN)

```


```python
# Declaración de una tupla

# Tiene 3 posiciones, comenzado en el 0. Largo de 3

calificaciones = (8,7,9) 

print(calificaciones)

print( type(calificaciones) ) 


```


```python
# vamos a acceder a cada dato

calificacion1 = calificaciones[0]
calificacion2 = calificaciones[1]
calificacion3 = calificaciones[2]

print(calificacion1)
print(calificacion2)
print(calificacion3)
```


```python
# Recorriendo tuplas con for y while

for calificacion in calificaciones:
    print(calificacion)
    
print('-------------------------')

contador = 0

while contador < len(calificaciones):
    calificacion = calificaciones[contador]
    print(calificacion)
    contador += 1
```

## Listas

Es una colección de elementos ordenados. En otro lenguajes es conocido como un `array`. A este tipo de colección es Mutable, es decir, se le pueden agregar, eliminar, quitar, elementos. Podemos hacer diversas operaciones con ellos.

Elementos que debemos tener en cuenta son:

- `index`: El indice o posición de cada elemento en la lista, recordar que todas comienzan en la posición 0.
- `length`: La longitud o cantidad de elementos que contiene la lista

**Sintaxis**

```python
nombre_lista = [elemento1, elemento2, elemento3,.. , elementoN]
```

### Como se deben nombrar las listas (buena practica o convension)

- El nombre de la varable que contanga una lista, debe ser en **plural**
- Puede contener la palabra **\*\*_list\*\*** o **\*\*_list\*\***


### Funciones de las listas

Las lista son un objeto, por lo tanto cuenta con diversos metodos los cuales nos ayudan a interactuar con ellos:

- `append(element)`:	Adds an element at the end of the list
- `clear()`:	Removes all the elements from the list
- `copy()`:	Returns a copy of the list
- `count(element)`:	Returns the number of elements with the specified value
- `extend(list)`:	Add the elements of a list (or any iterable), to the end of the current list
- `index(element[,start[,end]])`:	Returns the index of the first element with the specified value
- `insert(<position, element)`:	Adds an element at the specified position
- `pop([index])`:	Removes the element at the specified position
- `remove(element)`:	Removes the first item with the specified value
- `reverse()`:	Reverses the order of the list
- `sort()`:	Sorts the list


```python
# Declaro una lista con unas materias
materias = ['analogicas', 'digitales', 'mediciones'] # lista de str

print(materias)

#agregamos una materia mas a la lista
materias.append('dibujo 3D')

#imprimo la lista
print(materias)

#creo otra lista
materias2 = ['neumatica', 'mecanismos']

# Extendemos la primer lista con la segunda
materias.extend(materias2)

#imprimo la lista
print(materias)

#inserto una materia en la posición 2
materias.insert(2,'Matematicas')

#imprimo la lista
print(materias)

#removemos el elemento 'Matematicas'
materias.remove("Matematicas")

#imprimo la lista
print(materias)

# Ordenamos las lista
materias.sort()

#imprimo la lista
print(materias)

# sacamos un elemento de la lista, si no se especifica saca al ultimo
ultima_materia = materias.pop()

#imprimo la lista
print(materias)

print('ultima materia:', ultima_materia)

# Invierto el orden de la lista
materias.reverse()

#imprimo la lista
print(materias)
```

    ['analogicas', 'digitales', 'mediciones']
    ['analogicas', 'digitales', 'mediciones', 'dibujo 3D']
    ['analogicas', 'digitales', 'mediciones', 'dibujo 3D', 'neumatica', 'mecanismos']
    ['analogicas', 'digitales', 'Matematicas', 'mediciones', 'dibujo 3D', 'neumatica', 'mecanismos']
    ['analogicas', 'digitales', 'mediciones', 'dibujo 3D', 'neumatica', 'mecanismos']
    ['analogicas', 'dibujo 3D', 'digitales', 'mecanismos', 'mediciones', 'neumatica']
    ['analogicas', 'dibujo 3D', 'digitales', 'mecanismos', 'mediciones']
    ultima materia: neumatica
    ['mediciones', 'mecanismos', 'digitales', 'dibujo 3D', 'analogicas']


### Obteniendo los datos de una lista

**Sintaxis**

```python
   
    variable = nombre_lista [ posicion ]

```


```python
#Acceso a los datos de la lista

materia1 = materias[0]
materia2 = materias[1]
materia3 = materias[2]
materia4 = materias[3]

print(materia1)
print(materia2)
print(materia3)
print(materia4)
```

    mediciones
    mecanismos
    digitales
    dibujo 3D



```python
# Recorriendo una lista con FOR

for materia in materias:
    print('La materia es: ', materia)

print('*********************')

# Recorriendo una lista con WHILE

count = 0

while count < len(materias):
    materia = materias[count]
    print('La materia es: ',materia)
    count +=1

```

    La materia es:  mediciones
    La materia es:  mecanismos
    La materia es:  digitales
    La materia es:  dibujo 3D
    La materia es:  analogicas
    *********************
    La materia es:  mediciones
    La materia es:  mecanismos
    La materia es:  digitales
    La materia es:  dibujo 3D
    La materia es:  analogicas



```python
# Cosas adicionales que se pueden realizar con listas

#obtener la suma de los valores contenidos en la lista

valores = [1,5,3,9,6,3,5,8,7,2,6,7,2,5,2,3,5,4,5]

suma = sum(valores)
maximo = max(valores)
minimo = min(valores)

print("La suma:", suma)
print("El valor maximo:", maximo)
print("El valor minimo:", minimo)
```

    La suma: 88
    El valor maximo: 9
    El valor minimo: 1


### Ejercicios

1. Crear una lista de frutas: *manzana*, *platano* y *melon*. Posteriormete agregar *sandia*. Despues agregarle una lista mas que contenga *papaya*, *kiwi* y *durazno*. He imprimir la lista completa. Despues remover la *sandia* e imprimir el resultado. Recorrer la lista de frutas imprimiendo cada una (usando un ciclo, de preferencia usar *for*).

2. Crear una lista con sus calificaciones de Neumatica, y obtener el promedio. Se debe utilizar la función `sum` para el procedimiento. Imprimir cual es la calificacion maxima y minima, usando las funciones `max()` y `min()`


## Eliminando elementos de la lista `del`

Cuando queremos eliminar algún elemento de una colección se usa la palabra reservada `del` junto a la posición del elemento a eliminar.

**Sintaxis**

-  `del colección[posicion|key]`


```python
# Eliminar elementos de una colección

materias = ['analogica', 'digitales', 'mediciones' ]

print(materias)

del materias[1] # Elimino el elemento que esta en la posición 1 de la colección

print(materias)


alumnos = { 'carlos':[8,8,9] , 'angel':[8,8,8] }

print(alumnos)

del alumnos['carlos']

print(alumnos)
```

    ['analogica', 'digitales', 'mediciones']
    ['analogica', 'mediciones']
    {'carlos': [8, 8, 9], 'angel': [8, 8, 8]}
    {'angel': [8, 8, 8]}


## Función `len`

Los iteradores por default no te dicen cual es su largo, en muchas ocasiones necesitamos saber el largo para realizar ciertas tareas, para eso Python trae una función que nos ayuda.

**Sintaxis**

- `len(iterator)`: Devuelve el numero de los elementos de una colección


```python
# Ejemplos de aplicacion de la función len()

string = 'hola'
str_len = len(string)

tupla = (5,9,3,6,'mensaje')
tupla_len = len(tupla)

lista = [1,2,3,6,'hola']
lista_len = len(lista)

diccionario = {'key1': 'valor1', 'key2': 'valor2', 'key3': 'valor3' }
dic_len = len(diccionario)

print('largo de str',str_len)
print('largo de tupla',tupla_len)
print('largo de lista',lista_len)
print('largo de diccionario',dic_len)
```

    largo de str 4
    largo de tupla 5
    largo de lista 5
    largo de diccionario 3



```python
especialidades = [
    'mecatronica',
    'laboratorio',
    'contanbilidad',
    'mecanica',
    'electricidad'
    ]

count = 0

while count < len(especialidades):
    especialidad = especialidades[count]
    print(f'Una de las especialidades es: {especialidad}')
    count+=1
```

    Una de las especialidades es: mecatronica
    Una de las especialidades es: laboratorio
    Una de las especialidades es: contanbilidad
    Una de las especialidades es: mecanica
    Una de las especialidades es: electricidad



```python
import random
#Creando un pesudobot

#declaramos una lista con las frases que queremos decir con nuestro bot
hobbies = ['leer', 'correr', 'nadar']


print('Hola, me llamo MecaBot')
print('Cual es tu nombre')
name = input()

print(f'Es un gusto concerte {name}')
print('Que lindo nombre tienes ;)')

print('Cual es tu hobby?')
hobby = input()

print(f'Wow!!!! que conincidencia, a mi tambien me encanta {hobby}')
print(f'Te cuento que tambien me gusta mucho {random.choice(hobbies)}')

```

    Hola, me llamo MecaBot
    Cual es tu nombre
    Jose
    Es un gusto concerte Jose
    Que lindo nombre tienes ;)
    Cual es tu hobby?
    correr
    Wow!!!! que conincidencia, a mi tambien me encanta correr
    Te cuento que tambien me gusta mucho leer


## Diccionarios

Son un tipo de colección que su estructura es `Llave - Valor`. Para obtener el acceso al *valor* se hace a traves de la *llave*. La llave es unica y por lo tanto no se puede repetir.

**Sintaxis**

```python
# Creacion de un diccionario    
    diccionario = { 
        'llave1': 'str',
        'llave2' : 5
        'llave3' : True,
        'llave4' : [1,2,6,'a']
        ......        
    }
    
# Leyendo datos del diccionario

variable1 = diccionario['llave3'] # True
variable1 = diccionario.get('llave3') # True, en caso que no exista devuelve None

# Modificando valores existentes en el diccionario

diccionario['llave4'] = [1,2,6,8,5,6]

# Agregando valores nuevos al diccionario

diccionario['llave5'] = 'un valor'
```



```python
calificaciones_neumatica = {
    'gamas': 9,
    'angelo': 8,
    'dania' : 10    
}

print(calificaciones_neumatica['gamas'] )
print(calificaciones_neumatica['angelo'] )
print(calificaciones_neumatica['dania'] )

calificaciones_neumatica['leon'] = 10 # agregando un valor al diccionario

print(calificaciones_neumatica['leon'])

calificaciones_neumatica['angelo'] = 7 # actualizo el valor de esa llave

print(calificaciones_neumatica['angelo'])
```

    9
    8
    10
    10
    7



```python
for key in calificaciones_neumatica:
    print(f'con la llave: {key}, el valor es: {calificaciones_neumatica[key]}')

print('=======================')

# Extraigo todas las llaves
for key in calificaciones_neumatica.keys():
    print(key)

print('=======================')
    
# Extraigo los valores
for values in calificaciones_neumatica.values():
    print(values)
```

    con la llave: gamas, el valor es: 9
    con la llave: angelo, el valor es: 7
    con la llave: dania, el valor es: 10
    con la llave: leon, el valor es: 10
    =======================
    gamas
    angelo
    dania
    leon
    =======================
    9
    7
    10
    10


## Función de ordenamiento (`sorted`)

Esta función ordena los elementos de una colección.

```python

collection = [4,2,9,12,8]

ordenado = sorted(collection)

print(ordenado)

```

    [2,4,89,12]


https://developers.google.com/edu/python/sorting

## Función `tuple()`

La función tuple crea una instancia de una tupla vacía si no le pasamos ningún argumento. El argumento que puede recibir una colección.


```python
mi_tupla = tuple() # crea una tupla vacía

calificaciones = [8,6,9,6,8]

tupla_calificaciones = tuple(calificaciones)

type(mi_tupla)

print(calificaciones)
print(tupla_calificaciones)
```

    [8, 6, 9, 6, 8]
    (8, 6, 9, 6, 8)


## Función `list()`

La función list crea una instancia de una lista vacía si no le pasamos ningún argumento. El argumento que puede recibir una colección.


```python
lista_vacia = list()

print(lista_vacia)

tupla_calificaciones = (8, 6, 9, 6, 8)
lista_calificaciones = list(tupla_calificaciones)

print(tupla_calificaciones)
print(lista_calificaciones)
```

    []
    (8, 6, 9, 6, 8)
    [8, 6, 9, 6, 8]


## Función `dict()`

La función dict crea una instancia de un diccionario vacío si no le pasamos ningún argumento. El argumento que puede recibir una colección.


```python
mi_diccionario = dict()

print(mi_diccionario)

mi_diccionario['hola'] = 4

print(mi_diccionario)
```

    {}
    {'hola': 4}


## Función `enumerate()`

A esta función se le pasa un iterable y me devuelve 2 valores, en la primera posición me pasa el indice y en la segunda posición me pasa el valor que tiene en ese momento el iterador.


**Sintaxis:**

```python
index, value = enumerate(iterador)
```


```python
pokemons = ['pikachu', 'bolbasor', 'charizard' ]

# Forma fea y horrible
count = 0
for pokemon in pokemons:
    print(f'La posicion de {pokemon} es {count}')
    count +=1

print('===================================')

# La forma chida
for index, value in enumerate(pokemons):
    print(f'La posicion de {value} es {index}')
```

    La posición de pikachu es 0
    La posición de bolbasor es 1
    La posición de charizard es 2
    ===================================
    La posición de pikachu es 0
    La posición de bolbasor es 1
    La posición de charizard es 2

---

Realizado por Docente: [Alejandro Leyva](https://www.alejandro-leyva.com/)

[Mecatrónica 85](https://mecatronica85.com/)

[fb/mecatronica85](https://www.facebook.com/mecatronica85)
