from machine import Pin
from time import sleep

#lcd inputs
d7 = Pin(6, Pin.OUT)
d6 = Pin(7, Pin.OUT)
d5 = Pin(8, Pin.OUT)
d4 = Pin(9, Pin.OUT)

enable = Pin(10, Pin.OUT)
RS = Pin(11, Pin.OUT)

def send_command(bin_num):
  enable.high()
  RS.low()
  d4.value((bin_num & 0b0001) >> 0)
  d5.value((bin_num & 0b0010) >> 1)
  d6.value((bin_num & 0b0100) >> 2)
  d7.value((bin_num & 0b1000) >> 3)
  enable.low()

def send_data(bin_num):
  enable.high()
  RS.high()
  d4.value((bin_num & 0b0001) >> 0)
  d5.value((bin_num & 0b0010) >> 1)
  d6.value((bin_num & 0b0100) >> 2)
  d7.value((bin_num & 0b1000) >> 3)
  enable.low()

def initialize_lcd():
  send_command(0b0010)
  send_command(0b0010)
  send_command(0b0000)
  send_command(0b0000)
  send_command(0b1110)
  send_command(0b0000)
  send_command(0b0110)

def write_byte(byte):
  send_data((byte & 0b11110000) >> 4)
  send_data(byte & 0b00001111)

def write_message(message):
  for letter in message:
    write_byte(ord(letter))

initialize_lcd()
write_message("Hello World ")
while True:
  pass
