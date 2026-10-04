from machine import Pin, ADC, DAC, PWM
from time import sleep

velocidad = ADC(Pin(32))                    # Potenciometro | ADC 1 - GPIO 32
masa = ADC(Pin(25))                         # Potenciometro | ADC 2 - GPIO 25

start = Pin(18, Pin.IN, Pin.PULL_UP)        # Boton         | GPIO 18
presencia = Pin(22, Pin.IN, Pin.PULL_UP)    # Boton         | GPIO 22

led_run = Pin(23, Pin.OUT)                  # LED           | GPIO 23
led_alarma = Pin(27, Pin.OUT)               # LED           | GPIO 27

motor = PWM(Pin(5), freq=1000, duty=0)      # PWM           
dac = DAC(Pin(26))                          # DAC


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
    
    pwm_final = 0
    # BOTÓN: solo funciona si la máquina está encendida
    if maquina_encendida and presencia.value() == 0:
        
        vref = ((float(velocidad.read()))/4095)*2
        carga = ((float(masa.read()))/4095)*100
        
        dac_vref = int(vref/2*255)
        dac.write(dac_vref)
        
        pwm_ref = (vref/2)*100
        
        if carga<=95:
            led_run.value(1)
            if carga>80:
                pwm_final=0.5*pwm_ref
                led_alarma.value(1)
            else:
                pwm_final=pwm_ref
                led_alarma.value(0)
            print(f"Avanza;\tVelocidad: {vref:.2f} m/s;\tCarga: {carga:.2f} Kg; \tDAC: {dac_vref};  \tDuty: {pwm_final:.0f}")
        else:
            vref = 0.0
            print(f"Avanza;\tVelocidad: {vref:.2f} m/s;\tCarga: {carga:.2f} Kg; \tDAC: {dac_vref};  \tDuty: {pwm_final:.0f}")
            led_run.value(0)
            led_alarma.value(1)
            pwm_final=0
        motor.duty(int(pwm_final))
    else:
        motor.duty(0)
        led_run.value(0)
        led_alarma.value(0)
        pwm_final=0

    sleep(0.1)
