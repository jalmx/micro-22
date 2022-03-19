
# Entrada Analógica - ADC

El ESP8266 solo tiene una entrada analógica (GPIO 0) el cual puede leer un voltaje analógico y convertirlo a una valor digital.

Para configurar la entrada `GPIO` 0 como ADC:

```python
import machine # importo el modulo para control y configuración de pines

adc = machine.ADC(0) # configuro el GPIO0 como ADC o entrada analógica
```

Para leer el valor en el ADC se realiza con la función `read()`

```python
adc.read() # esta función nos retorna el valor que existe en la entrada
```

Los valores que puede devolver la función `read()` son entre `0` (para 0.0 volts) hasta `1024` (para 1.0 volts). 

!!! warning "ADC"
    El ADC solo soporta hasta un `1V` directamente, pero en la placa **ESP8266 Node MCU** tiene un divisor de tension que ajuste el voltaje de **0V a 3.3V**, entonces debemos de conocer esta relación para los cálculos que se realicen.
