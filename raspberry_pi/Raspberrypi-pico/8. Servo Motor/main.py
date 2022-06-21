import machine 
import utime
 
analog_value = machine.ADC(28) 
pwm = machine.PWM(machine.Pin(0, machine.Pin.OUT))
pwm.freq(60) 
# duty_u16=32768)
 
while True:
    reading = analog_value.read_u16()     
    print("Potentiometer value ",reading)
    pwm.duty_u16(reading//8)
    utime.sleep(0.2)
