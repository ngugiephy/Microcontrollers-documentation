from machine import Pin, I2C
from utime import sleep_ms

sdaPin = Pin(0)
sclPin = Pin(1)

#commands definition
LCD_FUNCTION_RESET  = 0x30
FUNCTION_SET        = 0x20
DISPLAY_ON          = 0x0F
ENTRY_MODE          = 0x06

#Pin definitions
RS_PIN              = 0x01 #Connected to P0 of i2c module
RW_PIN              = 0x02 #Connected to P1 of i2c module
ENABLE_PIN          = 0x04 #Connected to P2 of i2c module
BACKLIGHT           = 0x08 #Connected to P3 of i2c module

SHIFT_DATA          = 4

# backlight = 0x01

#Get address of lcd on 12c bus, by default it's 0x27
# lcd = i_2_c.scan()
# if len(lcd) == 0:
#  print("No lcd device !")
# else:
#   print(lcd[0])

lcd_memory = 8
lcd_address = 0x27

i_2_c = machine.I2C(0,sda=sdaPin, scl=sclPin, freq=400000)


def write_command(cmd):
  """
  This function is used in writing commands to the lcd such as clear, CGRAM Address. The RS pin
  is held low and the enable pin of the lcd transitions from a high to a low.
  """
  byte = (BACKLIGHT |
          (((cmd >> 4) & 0x0f) << SHIFT_DATA))
  i_2_c.writeto(lcd_address, bytes([byte | ENABLE_PIN]))
  i_2_c.writeto(lcd_address, bytes([byte]))
  byte = (BACKLIGHT |
          ((cmd & 0x0f) << SHIFT_DATA))
  i_2_c.writeto(lcd_address, bytes([byte | ENABLE_PIN]))
  i_2_c.writeto(lcd_address, bytes([byte]))

def write_data(data):
  """
  This function is used in writing data to the lcd, this occurs when the RS Pin is low, and the
  Enable pin transitions from high to low.
  """
  byte = (RS_PIN |
          BACKLIGHT |
          (((data >> 4) & 0x0f) << SHIFT_DATA))
  i_2_c.writeto(lcd_address, bytes([byte | ENABLE_PIN]))
  i_2_c.writeto(lcd_address, bytes([byte]))
  byte = (RS_PIN |
          BACKLIGHT |
          ((data & 0x0f) << SHIFT_DATA))
  i_2_c.writeto(lcd_address, bytes([byte | ENABLE_PIN]))
  i_2_c.writeto(lcd_address, bytes([byte]))

def write_message(message):
  """
  Displays a message to the lcd module
  """
  for letter in message:
    write_data(ord(letter))

def backlight_on():
  """
  Turns on the backlight
  """
  i_2_c.writeto(lcd_address, bytes([BACKLIGHT]))

def backlight_off():
  """
  Turns off the backlight
  """
  i_2_c.writeto(lcd_address, bytes([0]))


def init_commands(command):
  """
  This function is used in initial setup of the lcd. It is used in ressetting and setting
  mode of the lcd. The enable pin is transitioned from high to low 
  """
  byte = ((command >> SHIFT_DATA) & 0x0f) << SHIFT_DATA
  i_2_c.writeto(lcd_address, bytes([byte | ENABLE_PIN]))
  i_2_c.writeto(lcd_address, bytes([byte]))

def setup_lcd():
  """
  This function resets the lcd display, sets its to 4-bit mode.
  """
  init_commands(LCD_FUNCTION_RESET)
  sleep_ms(5)
  init_commands(LCD_FUNCTION_RESET)
  sleep_ms(5)
  init_commands(FUNCTION_SET)
  sleep_ms(5)
  write_command(DISPLAY_ON)
  sleep_ms(5)
  write_command(ENTRY_MODE)

setup_lcd()
write_message("Hello ")
sleep_ms(1000)
backlight_off()
sleep_ms(1000)

write_message("World!")
sleep_ms(1000)
backlight_on()
while True:
  pass