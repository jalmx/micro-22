![banner](../assets/banner.png)

# Concatenación de Strings

La concatenación es el poder agrupar, juntar, unir, fusionar, pegar cadenas de caracteres, es decir, "sumar" varios string para formar uno solo.

La concatenación es realiza con el símbolo del signo más `+`. 


## Concatenando con `+`

Tenemos variables tipo `str` en donde guardamos texto.

**Ejemplo**


```python
frase = "La mejor especialidad es: "
nombre = "Mecatronica"

frase_completa = frase + nombre

print(frase + nombre)
print(frase_completa)
```

    La mejor especialidad es: Mecatronica
    La mejor especialidad es: Mecatronica


## Función `str()`

En la concatenación básica solo se pueden concatenar tipos `str`, por lo tanto, si necesitamos hacer un paso previo para que el tipo de dato que no sea `str` se convierta a este tipo. Para ello contamos con función `str()` la cual realiza ese trabajo. 

La sintaxis es:

```python
str(object, encoding=encoding, errors=errors)
```
**Parámetros:**

- `object	Cualquier tipo de objeto`
- `encoding	El encoding del objeto. Por default es UTF-8`
- `errors	Especifica que si hay un error en el encoding, que debe hacer`
- `return: Regresa el dato en tipo str : (str)`

Entonces, si tenemos un tipo `int`, `float` o `boolean` primero debemos convertirlos a tipo `str`.

**Ejemplo:**

```python
frase = "Mi edad es: "
edad = 25
edad_str = str(25)

print(frase + edad)

```

## Concatenando otros tipos de datos.

Si queremos hacer una concatenación directa entre un tipo `str` y otro tipo de dato, nos saldrá un error de tipo, indicando que no se puede concatenar `str` con alguno otro tipo. 
Como se muestra a continuación:


```python
print("Mi edad es: " + 25)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-2-fb8333b91b59> in <module>
    ----> 1 print("Mi edad es: " + 25)
    

    TypeError: can only concatenate str (not "int") to str


Por lo tanto, debemos hacer esa conversión previa a la concatenación. 
Existen dos formas, tomamos el valor, realizamos la conversión y se guarda en otra variable o la forma directa.

**Ejemplo:**


```python
#Por partes
frase = "Mi edad es: "
edad = 25
edad_str = str(25)

print(frase + edad_str)
print("Mi edad es: " + edad_str)
```

    Mi edad es: 25
    Mi edad es: 25


*Vamos a realizar una combinación básica entre los tipos de datos básicos*



```python
# Declaro las variables
edad = 25
altura = 1.68
nombre = "Alejandro"
casado = False

#Las convierto a tipo str

edad_str = str(edad)
altura_str = str(altura)
casado_str = str(casado)

print("Mi nombre es " + nombre + ", mi edad es de " + edad_str + " anios," + "tengo una altura de " + 
      altura_str + " mi estado de casado es: " + casado_str ) 

print("Mi nombre es " + nombre + ", mi edad es de " + str(edad) + " anios," + "tengo una altura de " + 
      str(altura) + " mi estado de casado es: " + str(casado))

```

    Mi nombre es Alejandro, mi edad es de 25 anios,tengo una altura de 1.68 mi estado de casado es: False
    Mi nombre es Alejandro, mi edad es de 25 anios,tengo una altura de 1.68 mi estado de casado es: False


## Secuencias de espace

Las secuencias de espace son caracteres especiales para darle formato a las cadenas de texto (Strings).

Nombre|Simbolo|Secuencia de escape
:-|:-:|:-:
Backslash|\\| `\\`
Comilla simple|\'|`\'`
Comilla doble|\"|`\"`
Bell|(sonido)|`\a`
Retroceso||`\b`
Nueva línea|(enter)|`\n`
Carriage return|\r|`\r`
Tab horizontal|tab|`\t`
Tab vertical|tab vertical|`\v`

#### Salto de línea `\n`

Cuando queremos que el texto tenga un salto de línea (enter), tenemos la secuencia `\n`.


```python
mensaje = "Hola\nTexto en siguiente linea\nla siguiente linea"

print("\n" + mensaje + "\n")
```

    
    Hola
    Texto en siguiente linea
    la siguiente linea
    


#### Tabulación 

En ocasiones queremos tabular (sangría) nuestro texto para darle un acomodo se aplica `\t`


```python
mensaje = "Columa 1\tColumna2\tColumna 3\nColuma 1\tColumna2\tColumna 3"
print(mensaje)
```

    Columa 1	Columna2	Columna 3
    Columa 1	Columna2	Columna 3


#### Comillas

En python nos da una ventaja con respecto al uso de comillas simples y dobles por default.
Recordando que se pueden escribir Strings `str` con `"` y `'`. Pero vamos a ver la diferencia si queremos utilizar las comillas ya sean simple o doble dentro del mensaje que queremos transmitir; al igual la equivalencia de las secuencias de escape `\'` y `\"`.


```python
# Si que queremos usar las comillas simples en un string sin utilizar la secuencia de escape, debemos usar 
# la comilla doble para generar dicho string

mensajeDobleComilla = "hola 'este texto esta en comilla simple' , texto fuera de la comilla"
mensajeComillaSimple = 'hola \'este texto esta en comilla simple\' , texto fuera de la comilla '

print(mensajeDobleComilla)
print(mensajeComillaSimple)
```

    hola 'este texto esta en comilla simple' , texto fuera de la comilla
    hola 'este texto esta en comilla simple' , texto fuera de la comilla 



```python
# Si que queremos usar doble comilla en un string sin utilizar la secuencia de escape, debemos usar 
# la comilla simple para generar dicho string

mensajeComillaSimple = 'hola "este texto esta en doble comilla" texto fuera de la comilla '
mensajeDobleComilla = "hola \"este texto esta en comilla simple\" , texto fuera de la comilla"

print(mensajeDobleComilla)
print(mensajeComillaSimple)
```

    hola "este texto esta en comilla simple" , texto fuera de la comilla
    hola "este texto esta en doble comilla" texto fuera de la comilla 


#### Back Slash

En ocasiones necesitamos utilizar la diagonal (slash) en un texto, para esto existe la secuencia de escape slasj doble `\\`.


```python
# Utilizando slash en un texto, por ejemplo para rutas dentro de un string

mensaje = 'ruta\\carperta1\\carperta2\\archivo'

print(mensaje)
```

    ruta\carperta1\carperta2\archivo


## Formateo de Strings - función `format()`

Los `str` tienen una propiedad llamada `format()` con la cual podemos concatenar variables, se tienen en varias formas para realizar la concatenacion con este método. Retorna el `str` con el formato indicado. Las variables se colocaran automaticamente en la llaves.

**Sintaxis:**

```python
'string {} ... {} ... '.format(variable1, variable2,...)

'string {0} ... {1} ... '.format(variable1, variable2,...)

'string {variable1} ... {variable2} ... '.format(variable1 ="hola", variable2=5,...)
```


```python
# La forma que es por default sin indicar nada, en el orden que los pasamos, seran asignados
nombre = "Alejandro"
edad = 30

texto_default = "Mi nombre es {} y tengo {} anios de edad".format(nombre, edad)

print(texto_default)
```

    Mi nombre es Alejandro y tengo 30 anios de edad



```python
# Formato indicando la varible en las llaves, esto sirve para cambiar el orden

color = "Rojo"
numero = 3

texto = "El numero '{1}' corresponde al color '{0}'".format(color, numero)

print(texto)
```

    El numero '3' corresponde al color 'Rojo', con el numero 3



```python
# Indicando el nombre de la variable 

texto_variables = "Mi nombre es {nombre} tengo {edad} anios".format(nombre="Alejandro", edad = 25)

print(texto_variables)
```

    Mi nombre es Alejandro tengo 25 anios


#### Formato para números y la precision

En muchas ocasiones queremos imprimir un valor numerico pero con cierta cantidad decimales, con la función `format()` nos da un formato para especificar como queremos la salida.

Debemos marcar una sintaxis especial que sigue el siguiente formato, principalmente es para valores flotantes:

**Sintaxis:**

```
[index]:[width][.precision][type]
```

**Tipos:**

- `d` para enteros
- `f` para flotantes
- `b` para números binarios
- `o` para números octal
- `x` para números hexadecimal
- `s` para strings
- `e` para flotante en formato exponente 

**Aplicado:**

```python

"El precio es {0:1.2f}".format(25.365894) #es la primera posición [0]

```



```python
#es la primera posición [0], parte entera como minimo un valor, con 2 decimales y tomarlo como tipo flotante
numero = 561.265264161
valor1 = "El precio es {0:1.2f}".format(numero)

# los valores enteros no es necesario indicar la parte decimal, solo se indica la posición
valor2 = "La calificacion final es {0:1.2f} de {1:1.1f} parciales".format(8.369,3)

print(valor1)
print(valor2)
```

    El precio es 561.27
    La calificacion final es 8.37 de 3.0 parciales



```python
valor1 = float(input('Dar valor 1: '))
valor2 = float(input('Dar valor 2: '))

suma = valor1 + valor2

print('El resultado es {0:1.3f}'.format(suma))
```

    Dar valor 1: 2.56256
    Dar valor 2: 2.6839
    El resultado es 5.246



```python
# Dar formato con decimales de forma dinámica
valor = float(input('Dar un valor para redondear: '))
redondeo = int(input('A cuantos decimales?: '))

r = '0:1.{}f'.format(redondeo)
msg = 'El valor redondeado a {1} decimales es: {' + r + '}'

print(msg)
print(msg.format(valor, redondeo))
```

    Dar un valor para redondear: 25.0
    A cuantos decimales?: 20
    El valor redondeado a {1} decimales es: {0:1.20f}
    El valor redondeado a 20 decimales es: 25.00000000000000000000



```python
nombre = "Alejandro"

print("Mi nombre es {0:s}".format(nombre))
```

    Mi nombre es Alejandro


## `f'String'`

Actualmente se tiene una nueva forma para crear strings de forma mas sencilla y dar formato.

**Esta es la forma mas actual que se usa.**

**Sintaxis:**

```python
cantidad = 5
color = "verde"

f'El numero de autos es {cantidad} y todos son color {color}'
f"El numero de autos es {cantidad} y todos son color {color}"
```


```python
cantidad = 5
color = "tutifruti"

mensaje1 = f'El numero de autos es {cantidad} y todos son color {color}'
mensaje2 = f"El numero de autos es \"{cantidad}\" y todos son color \"{color}\""

print(mensaje1)
print(mensaje2)
```

    El numero de autos es 5 y todos son color tutifruti
    El numero de autos es "5" y todos son color "tutifruti"


#### Formato a números con `f'string'`

**Sintaxis:**

```
{variable:{width}.{decimal-1}}
```

**Aplicacion:**

```python
num = 3.141592

print(f"El valor de pi es: {num:{1}.{3}}")
```


```python
# Es similar a la función format(), con respecto a la sintaxis, no es necesario indicar la posición de la variable
# los decimales es el valor menos 1

num = 3.14159
texto_formateado = f"El valor de pi es: {num:{1}.{3}}" # queremos 2 decimales
print(texto_formateado)

```

    El valor de pi es: 3.14


---
Realizado por Docente: [Alejandro Leyva](https://www.alejandro-leyva.com/)

[Mecatrónica 85](https://mecatronica85.com/)

[fb/mecatronica85](https://www.facebook.com/mecatronica85)
