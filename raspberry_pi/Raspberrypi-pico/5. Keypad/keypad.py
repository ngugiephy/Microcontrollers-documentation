from machine import Pin
from time import sleep_ms

row_1 = Pin(0, Pin.OUT)
row_2 = Pin(1, Pin.OUT)
row_3 = Pin(2, Pin.OUT)
row_4 = Pin(3, Pin.OUT)

col_1 = Pin(4, Pin.IN, Pin.PULL_DOWN)
col_2 = Pin(5, Pin.IN, Pin.PULL_DOWN)
col_3 = Pin(6, Pin.IN, Pin.PULL_DOWN)
col_4 = Pin(7, Pin.IN, Pin.PULL_DOWN)

key = [['1', '2', '3', 'A'], ['4', '5', '6', 'B'], ['7', '8', '9', 'C'], ['*', '0', '#', 'D']]

def is_key_pressed(col_1_value, col_2_value, col_3_value, col_4_value):
  if (col_1_value | col_2_value | col_3_value | col_4_value) == 0:
    return False
  else:
    return True

def key_pressed(row, col_1_value, col_2_value, col_3_value, col_4_value):
  if col_1_value == 1:
    return key[row - 1][0]
  elif col_2_value == 1:
    return key[row - 1][1]
  elif col_3_value == 1:
    return key[row - 1][2]
  elif col_4_value == 1:
    return key[row - 1][3]

while True:
  row_1.high()
  col_1_value = col_1.value()
  col_2_value = col_2.value()
  col_3_value = col_3.value()
  col_4_value = col_4.value()

  if is_key_pressed(col_1_value, col_2_value, col_3_value, col_4_value):
    print(key_pressed(1, col_1_value, col_2_value, col_3_value, col_4_value))
    sleep_ms(200)
  
  row_1.low()

  row_2.high()
  col_1_value = col_1.value()
  col_2_value = col_2.value()
  col_3_value = col_3.value()
  col_4_value = col_4.value()

  if is_key_pressed(col_1_value, col_2_value, col_3_value, col_4_value):
    print(key_pressed(2, col_1_value, col_2_value, col_3_value, col_4_value))
    sleep_ms(200)

  row_2.low()

  row_3.high()
  col_1_value = col_1.value()
  col_2_value = col_2.value()
  col_3_value = col_3.value()
  col_4_value = col_4.value()

  if is_key_pressed(col_1_value, col_2_value, col_3_value, col_4_value):
    print(key_pressed(3, col_1_value, col_2_value, col_3_value, col_4_value))
    sleep_ms(200)

  row_3.low()

  row_4.high()
  col_1_value = col_1.value()
  col_2_value = col_2.value()
  col_3_value = col_3.value()
  col_4_value = col_4.value()

  if is_key_pressed(col_1_value, col_2_value, col_3_value, col_4_value):
    print(key_pressed(4, col_1_value, col_2_value, col_3_value, col_4_value))
    sleep_ms(200)
  row_4.low()

