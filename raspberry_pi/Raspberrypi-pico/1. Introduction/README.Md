# INTRODUCTION TO RASPBERRY PI PICO

![Image](./The_board.png)

The raspberry pi pico is raspberry pi's first board based on a single microcontroller chip. It is designed for computing like the arduino.

---

## KEY FEATURES

Some of it's key features are:

- Memory features:

  1. 264KB on-chip RAM
  2. Upto 16MB of external RAM
  3. DMR controller for faster memory access

- 26x [GPIO pins](https://www.howtogeek.com/787928/what-is-gpio/)
- 3x analog input pins
- Hardware peripherals

  1. 2x [UART modules](https://pinout.xyz/pinout/uart)
  2. 2x [SPI controller](https://www.mathworks.com/help/supportpkg/raspberrypiio/ug/about-spi-interface-on-the-raspberry-pi-hardware.html)
  3. 2x [12c controllers](https://microcontrollerslab.com/raspberry-pi-pico-i2c-communication/#:~:text=I2C%20bus%20supports%20multiple%20slave,the%20master%20and%20the%20slave.)
  4. 16x [PWM channels](https://microcontrollerslab.com/raspberry-pi-pico-pwm-micropython-tutorial/#:~:text=Raspberry%20Pi%20Pico%20microcontroller%20contains,get%20any%20PWM%20signal%20output.)
  5. 1x USB1.1 with PHY

- Accelerated intager abd floating point arithmetic libraries.
- Power requiremements:
  1. 1.8v - 5.5v PC
  2. Low Power Modes
- Temperature sensor
- [On-chip RTC](https://www.waveshare.com/pico-rtc-ds3231.htm#:~:text=The%20Pico%2DRTC%2DDS3231%20is,thanks%20to%20the%20stackable%20design.&text=Raspberry%20Pi%20Pico%20is%20NOT%20included.)
- Special hardware features:
  1. Micro-USB B port for power and data (and for reprogramming the Flash)
  2. Onboard LED
  3. Boot select push button

If you need to know the pin numbers for the raspberry pi pico you can refer to the following diagram:

![IMAGE](./the_pins_intro.png)

If you need to simulate some simple projects,you can check out [here](https://wokwi.com/)

---

## PROGRAMMING THE RASPBERRY PI PICO

Has C/C++ toolchain for the RP2040 microcontroller.
It is also capable of running [Micropython](https://www.digikey.com/en/maker/projects/micropython-basics-what-is-micropython/1f60afd88e6b44c0beb0784063f664fc) framework.

You will need to [install thonny](https://thonny.org/) in order to program the raspberry pi pico. For linux users, thonny can be installed using the command:

   <p align="center">
   sudo apt-get -y install thonny
   </p>

You can check whether you've installed thonny using the command:

 <p align="center">
which thonny
</p>

For the lovers of Visual Studio Code, you can also use it to program the raspberry pi pico. Just follow [these steps](https://www.youtube.com/watch?v=3Uy9ySoMXAY) to get started.

Once you're done, you can head over to the next step.
