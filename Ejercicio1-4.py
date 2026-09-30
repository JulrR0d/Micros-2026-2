from machine import Pin, ADC, DAC, PWM
from time import sleep
velocidad = ADC(Pin(32))                    # Potenciometro | ADC 1 - GPIO 32
masa = ADC(Pin(25))                         # Potenciometro | ADC 2 - GPIO 25
start = Pin(34, Pin.IN, Pin.PULL_UP)        # Boton         | GPIO 34
presencia = Pin(22, Pin.IN, Pin.PULL_UP)    # Boton         | GPIO 22
led_run = Pin(23, Pin.OUT)                  # LED           | GPIO 23

maquina_encendida = False

while True:

    # START: cambia entre encendido y apagado
    if start.value() == 0:
        maquina_encendida = not maquina_encendida

        if maquina_encendida:
            print("Máquina encendida")
        else:
            print("Máquina apagada")
            led_run.value(0)

        sleep(0.3)   # evita múltiples cambios por una pulsación

    # BOTÓN: solo funciona si la máquina está encendida
    if maquina_encendida and presencia.value() == 0:
        print("Avanza")
        led_run.value(1)
    else:
        led_run.value(0)

    sleep(0.1)