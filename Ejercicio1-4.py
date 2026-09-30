from machine import Pin
from time import sleep
start = Pin(18, Pin.IN, Pin.PULL_UP)
boton = Pin(22, Pin.IN, Pin.PULL_UP)
led = Pin(23, Pin.OUT)

maquina_encendida = False

while True:

    # START: cambia entre encendido y apagado
    if start.value() == 0:
        maquina_encendida = not maquina_encendida

        if maquina_encendida:
            print("Máquina encendida")
        else:
            print("Máquina apagada")
            led.value(0)

        sleep(0.3)   # evita múltiples cambios por una pulsación

    # BOTÓN: solo funciona si la máquina está encendida
    if maquina_encendida and boton.value() == 0:
        print("Avanza")
        led.value(1)
    else:
        led.value(0)

    sleep(0.1)