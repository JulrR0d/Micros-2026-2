from machine import DAC, Pin, ADC, PWM
vRef = ADC(Pin(4))# Potenciometro 1 - ADC 2
carga = ADC(Pin(34)) # Potenciometro 2 - ADC 1
start = Pin(22, Pin.IN, Pin.PULL_UP) # Boton 1
precencia = Pin(23, Pin.IN, Pin.PULL_HOLD) # Boton 2
run = Pin(21, Pin.OUT) # LED verde
sobrecarga = Pin(15, Pin.OUT)# LED rojo
#DAC
#PWM

def inicio(Pin):
    run.value(not run.value())
    while (True):



start.irq(
    trigger=Pin.IRQ_FALLING,
    handler=inicio
)
