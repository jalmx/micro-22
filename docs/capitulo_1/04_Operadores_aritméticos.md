![banner](../assets/banner.png)

# Operadores aritméticos

En Python contamos con varios operadores aritméticos.

| Nombre          | Símbolo | Ejemplo |
| :-------------- | :-----: | ------- |
| Suma            |    +    | 4 + 2   |
| Resta           |    -    | 4 - 5   |
| Negación        |    -    | -2      |
| Multiplicación  |    *    | 6 * 8   |
| División        |    /    | 1 / 2   |
| División entera |   //    | 5 // 3  |
| Exponente       |   **    | 4\**2   |
| Módulo          |    %    | 5 % 2   |


```python
print("Suma")
print( 4 + 2)
print("-------")
print("Resta")
print( 4 - 2)
print("-------")
print("Negación")
a = 2
print( -a) # -1 * a
print("-------")
print("Multiplicación")
print( 4 * 2)
print("-------")
print("División")
print( 1/2)
print("-------")
print("División entera")
print( 10//3)
print("-------")
print("Exponente")
print( 3**2) # 3^2
print("-------")
print("Módulo o Residuo") 
print(10 % 3) # 10%3 = 1
```

##  Precedencia de operadores

El orden de precedencia de ejecución de los operadores aritméticos es:

| Orden | Operador |
| :---- | :------- |
0. Agrupación | ( )
1. Exponente | \**
2. Negación | -
3. Multiplicación , División, División entera, Módulo |*, /, //, %
4. Suma , Resta | +, -


## Ejemplos:

Convertir la expresión algebraica, a una expresión computable

1. $\frac{2-3}{20}$
2. $3 \times \frac{1}{2} + 8$
3. $3^2 + 6^3 - \frac{5}{10}$
4. $\frac{5 + 6 \times 9}{6 \times 1} + 3 - \frac{8}{2}$
5. $\frac{6+8}{2*3-5}$


```python
caso_1 = (2-3) / 20
caso_2 = 3 * (1/2) + 8
caso_3 = (3**2) + (6**3) - (5/10)
caso_4 = ((5+(6*9)) / (6*1)) + 3 - (8/2)
caso_5 = (6+8)/((2 * 3)- 5) 

print("Resultado caso 1: " + str(caso_1) )
print("Resultado caso 2: " + str(caso_2) )
print("Resultado caso 3: " + str(caso_3) )
print("Resultado caso 4: " + str(caso_4) )
print("Resultado caso 5: " + str(caso_5) )
```

## Ejercicios

Guardar en una variable el resultado de la operación e imprimir por consola el resultado de las siguientes operaciones:

1. $\frac{5 + 8}{2}$
2. $\frac{5 }{2} + 3$
3. $5 + \frac{1}{2} \times 6$
4. $5^2$
5. $3 + \frac{1}{2} \times \frac{5}{-2}$

##  Aplicaciones

Vamos resolver unos problemas basicos

1. Realizar una calculadora que sume 2 números, los valores están en el programa
2. Realizar una calculadora que haga la división de 2 números, los valores están en el programa
3. Realizar el cálculo de voltaje, los valores están en el programa


```python
# 1. Realizar una calculadora que sume 2 números que esten en el programa

valor_1 = 15
valor_2 = 269

suma = valor_1 + valor_2

print("La suma de " + str(valor_1) + " con " + str(valor_2) + " es: " 
      + str(suma))
```

    La suma de 15 con 269 es: 284



```python
# 2. Realizar una calculadora que haga la división de 2 números, los valores están en el programa
valor_1 = 5
valor_2 = 20

division = valor_1 / valor_2

print("La division de " + str(valor_1) + " entre " + str(valor_2) +
      " es: " + str(division))
```

    La division de 5 entre 20 es: 0.25



```python
# 3. Realizar el cálculo de voltaje, los valores estan en el programa
corriente = 0.01 # 10mA
resistencia = 1000 #1k

voltaje = corriente * resistencia

print("La corriente es " + str(corriente) + "A, la resistencia es: " + str(resistencia) 
      + " Ohms, el voltaje es: " + str(voltaje) + "V")
```

    La corriente es 0.01A, la resistencia es: 1000 Ohms, el voltaje es: 10.0V


###  Ejercicios

- Segunda Ley, calcular fuerza con datos guardados. Formula $F = m * a$
- Hacer la operación de 5 resistencias en serie, dar resistencia total
- Hacer el calculo de 5 resistencias en paralelo, dar resistencia total


---
Realizado por Docente: [Alejandro Leyva](https://www.alejandro-leyva.com/)

[Mecatrónica 85](https://mecatronica85.com/)

[fb/mecatronica85](https://www.facebook.com/mecatronica85)
