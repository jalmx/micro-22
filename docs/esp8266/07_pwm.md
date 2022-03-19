---
title: Salida analógica - PWM
---

# Salida analógica PWM

Pulse width modulation (PWM) is a way to get an artificial analog output on a digital pin. It achieves this by rapidly toggling the pin from low to high. There are two parameters associated with this: the frequency of the toggling, and the duty cycle. The duty cycle is defined to be how long the pin is high compared with the length of a single period (low plus high time). Maximum duty cycle is when the pin is high all of the time, and minimum is when it is low all of the time.

On the ESP8266 the pins 0, 2, 4, 5, 12, 13, 14 and 15 all support PWM. The limitation is that they must all be at the same frequency, and the frequency must be between 1Hz and 1kHz.

To use PWM on a pin you must first create the pin object, for example:

To use PWM on a pin you must first create the pin object, for example:

    import machine
    p12 = machine.Pin(12)

Then create the PWM object using:


    pwm12 = machine.PWM(p12)

You can set the frequency and duty cycle using:

    pwm12.freq(500)
    pwm12.duty(512)

http://docs.micropython.org/en/latest/esp8266/tutorial/pwm.html

PWM can be enabled on all pins except Pin(16). There is a single frequency for all channels, with range between 1 and 1000 (measured in Hz). The duty cycle is between 0 and 1023 inclusive.