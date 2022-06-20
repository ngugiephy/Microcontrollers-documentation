import machine
from math import log
import utime
 
analog_value = machine.ADC(28)

BETA = 3950 # should match the Beta Coefficient of the thermistor
 
while True:
    reading = analog_value.read_u16()
    celsius = 1 / (log(1 / (65535. / reading - 1)) / BETA + 1.0 / 298.15) - 273.15;     
    print("ADC: ",celsius)
    #Read in intervals of 2 seconds
    utime.sleep(2) 
