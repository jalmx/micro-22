# Ejercicios con ADC

- Leer un potenciómetro y mostrarlo en terminal
- Leer LDR

## Ejemplos control de entradas analógicas

!!! example "Ver el valor del ADC por la terminal"
    - **Descripción:** Encender el led configurando un pin como salida D1
    - **Material:** 
        - 1 Potenciómetro
    - **Diagrama:** <br>![adc_1](imgs/adc_0.png)
    - **Código:** 
        ```python
        import machine # importo el modulo para control y configuración de pines
        from time import sleep

        adc = machine.ADC(0) # configuro el GPIO0 como ADC o entrada analógica
        
        valor = adc.read() # esta función nos retorna el valor que existe en la entrada

        print(valor) # mando a la terminal el valor del ADC
        sleep(1) # espero un segundo
        ```