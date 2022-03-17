![banner](../assets/banner.png)

# Variables en Python

*Python es un lenguaje dinamicamente tipado, y sin declaración de tipo, tan solo se declara la variable con un valor de inicialización, es lo **único necesario**.*

## Buenas prácticas para declaración de variables en Python

En Python las buenas practicas que se aplican a la declaración de variables, son las siguientes:

- Se deben escribir en minúsculas
- Solo puede contener números después de la primera letra con el que comienza el nombre de la variable que estamos declarando.
    - Ejemplo:
        - `k5m`
        - `variable1`
        - `v2s`
        - `variable_2`
- Sensibles a minúsculas y mayúsculas; es decir, si declaro una variable llamada `variable1` y otra llamada `Variable1`, para la computadora son variables o espacios de memoria distintos, aun que suenen igual, con el solo hecho de cambiar una letra, ya estamos hablando de una variable distinta.
- No pueden contener espacios entre letras o palabras
- No puede comenzar con números o símbolos
- No puede contener caracteres especiales, todos son caracteres especiales menos el abecedario ingles. Ejemplo: !"·\$%&\/()=?¿.
- **El nombre debe ser descriptivo**; es decir, con solo leerlo podemos deducir qué hace o para qué fue declarada
- *(Regla especial):* Todo de escribe en ingles.
- Si se desea escribir una variable combinando dos palabras o más, se separarán con un guión bajo (_). Esta **convensión** se llama **Snake Case** (snake_case)
    - Ejemplos:
        - `valor`
        - `valor1`
        - `valor_uno`
        - `valor_1`
- **Siempre se debe inicializar la variable**:
    - Ejemplo: 
        - `mi_variable = 10`
        - `variable_2 = "mensaje"`

## Tipos de datos en Python

Al ser un lenguaje dinamicamente tipado no es necesario indicar que tipo es variable, pero se deben conocer para la compatibilidad de tipos y cómo podemos trabajar con ellos.

Tipo | Descripción | Ejemplo
:-:|:-|:-
Int| Números enteros naturales | `variable_int = 10`
Float| Números con punto decimal | `variable_flotante = 2.2`
str|Cadena de caracteres (String)| `variable_str = "texto"`
Bool|Tipo booleano | `variable_bool = True`
Complex| Tipo número complejo | `variable_complex = 3+5j`
(Int) Hexadecimal|Número hexadecimal |`variable_hex = 0xa`
(Int) Octal|Número octal | `variable_oct =  0o12`
(Int) Binario| Número binario | `variable_bin = 0b1010`

## Variables tipo Enteras (int)

El tipo de variable más común son las variables enteras, que son valores tanto *negativos o positivos enteros*. Prácticamente no hay límite con el valor que se puede asignar, siempre y cuando no tenga parte fraccionaria.

**Ejemplo:**


```python
variable = 10 # Inicializo con un valor de 10

variable_2 = 0 # Inicializo con un valor de 0

variable_3 = -5 # Inicializo con un valor de -5

valor_enorme = 5000000000000000000000000000000000000000000000000000000
```


```python
print(variable)
print("-----")
print(variable_2)
print("-----")
print(variable_3)
print("-----")
print(valor_enorme)
```

    10
    -----
    0
    -----
    -5
    -----
    5000000000000000000000000000000000000000000000000000000


Dentro de la variables enteras también están comprendidas otro números con base diferente, siempre manejamos base decimal. En el ejemplo que se muestra asignación de otros tipos de variables.


```python
diez = 10               # Base diez, comprende de 0 a 9

diez_binario = 0b1010   # Número binario, comprende de 0 y 1

diez_octal = 0o12       # Base Octal, comprende de 0 a 7

diez_hex = 0x0a          # Base hexadecimal comprende de 0 a F
```


```python
print(diez)
print("-----")
print(diez_binario)
print("-----")
print(diez_octal)
print("-----")
print(diez_hex)
```

    10
    -----
    10
    -----
    10
    -----
    10


## Variables tipo Flotantes (float)

El tipo de variable flotante o punto flotante, que son valores tanto *negativos o positivos con parte decimal*. Prácticamente no hay límite con el valor que se puede asignar.

**Ejemplo:**


```python
variable = 5.6 # Inicializo con un valor de 5.6

variable_2 = 0.4 # Inicializo con un valor de 0.4

variable_3 = -5.4 # Inicializo con un valor de -5.4

variable_4 = 0.000000000000000005616516851654864651
```


```python
print(variable)
print("-----")
print(variable_2)
print("-----")
print(variable_3)
print("-----")
print(variable_4)
print("-----")
```

    5.6
    -----
    0.4
    -----
    -5.4
    -----
    5.616516851654865e-18
    -----


## Variables tipo str (String) o Cadena de caracteres

Otro tipo de dato utilizado es el tipo de dato String, abreviado `str`.
Hay varias formas para crear este tipo de dato, se debe escribir entre doble comilla `""`, entre doble comilla simple `''`, entre tripe comilla simple `''' '''`, entre triple dobles comillas `""" """` 


```python
cadena_1 = 'This is a string in Python' # string in single quotes
cadena_2 = "This is a string in Python" # string in double quotes
cadena_3 = '''This is a string in Python''' # string in triple quotes
cadena_4 = """This is a string in Python""" # string in triple double-quotes
```


```python
print(cadena_1)
print("----------------")
print(cadena_2)
print("----------------")
print(cadena_3)
print("----------------")
print(cadena_4)
```

    This is a string in Python
    ----------------
    This is a string in Python
    ----------------
    This is a string in Python
    ----------------
    This is a string in Python


En concreto entre doble comilla y comilla simple no hay diferencias pero con lo que respecta a triple comilla simple y triple comilla doble, se conoce como multilinea.


```python
str1='''This is 
the first
Multi-line string.
'''
print(str1)

str2="""This is
the second
Multi-line
string."""
print(str2)
```

No se pueden mezclar entre doble comilla y simple comilla, y tienen efectos similares, es decir, si necesitamos mostrar un texto con comillas simples o doble comilla, se realiza de la siguiente manera.


```python
str1='Estamos aprendiendo "Python" paso a paso'
print(str1)

str2="Estamos aprendiendo 'Python' paso a paso"
print(str2)
```

    Estamos aprendiendo "Python" paso a paso
    Estamos aprendiendo 'Python' paso a paso


## Variables tipo Booleana (bool)

El tipo de dato booleano solo tiene dos tipos de valores:
- `True`
- `False`

Creamos unas variables y asignamos valores tipo booleanos.

**Ejemplo:**


```python
valor_verdadero = True

valor_falso = False

print(valor_verdadero)
print('----------')
print(valor_falso)
```

    True
    ----------
    False

---

Realizado por Docente: [Alejandro Leyva](https://www.alejandro-leyva.com/)

[Mecatrónica 85](https://mecatronica85.com/)

[fb/mecatronica85](https://www.facebook.com/mecatronica85)
