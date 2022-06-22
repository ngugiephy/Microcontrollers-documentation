from machine import Pin
from time import sleep_us, sleep

class DistanceSensor:

  def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):
    """
    trigger_pin: Output pin to send pulses
    echo_pin: Readonly pin to measure the distance. The pin should be protected with 1k resistor
    echo_timeout_us: Timeout in microseconds to listen to echo pin. 
    By default is based in sensor limit range (4m)
    """
    self.trigger_pin = Pin(trigger_pin, Pin.OUT)
    self.trigger_pin.value(0)
    self.echo_pin = Pin(echo_pin, Pin.IN)
    self.echo_timeout_us = echo_timeout_us

  def trigger(self):
    """
    Send the pulse to trigger and listen on echo pin.
    We use the method `machine.time_pulse_us()` to get the microseconds until the echo is received.
    """
    self.trigger_pin.value(0)
    self.trigger_pin.value(1)
    sleep_us(10)
    self.trigger_pin.value(0)

    try:
      pulse_time = machine.time_pulse_us(self.echo_pin, 1, self.echo_timeout_us)
      return pulse_time
    except OSError as ex:
      if ex.args[0] == 110: # 110 = ETIMEDOUT
          raise OSError('Out of range')
      raise ex

  def get_distance_cm(self):
    # To calculate the distance we get the pulse_time and divide it by 2 
    # (the pulse walk the distance twice) and by 29.1 becasue
    # the sound speed on air (343.2 m/s), that It's equivalent to
    # 0.034320 cm/us that is 1cm each 29.1us
    pulse_time = self.trigger()
    distance_cm = (pulse_time / 2) / 29.1

    return distance_cm


#################################################################################

distance_sensor = DistanceSensor(0, 1)

while True:
  print(distance_sensor.get_distance_cm())
  sleep(2)




