from machine import Pin
from time import sleep

ledPin = Pin(5, Pin.OUT)
pushButton = Pin(0, Pin.IN, Pin.PULL_DOWN)
ledPin.high()

while True:
  pushButton_value = pushButton.value()
  ledPin_value = ledPin.value()
  if pushButton_value == 1:
    if ledPin_value == 1:
      ledPin.low()
    else:
      ledPin.high()