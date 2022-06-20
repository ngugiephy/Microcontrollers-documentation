# Blinking onboard LED 
The raspberry pi pico has an onboard LED on the pin 25 
## What you will need 
1. Thonny IDE(download from [here](https://thonny.org/))
2. [Micropython firmware](https://micropython.org/resources/firmware/rp2-pico-20220117-v1.18.uf2)
3. A usb cable for connecting to the pico.
### Steps 
- Download and install thonny IDE 
- While holding down the BOOTSEL button connect the pico to the computer. It should have shown up as a mass storage device.
![here](./rp2-pico.jpg)
- Copy and paste the downloaded uf2 file from [micropython page](https://micropython.org/resources/firmware/rp2-pico-20220117-v1.18.uf2)
- It is now ready to be used within thonny.
- Change the interpreter in your IDE by navigating to Run > Select Interpreter and select from the dropdown menu micropython(Raspberry pi pico)
- Run the [code](./simpleblink.py) you can change the value of delay by changing the value of 
``` python
time.sleep(1)
``` 
 
# Blinking external LED
- The steps above are used