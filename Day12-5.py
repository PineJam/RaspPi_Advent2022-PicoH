# Imports
import time
from machine import Pin, ADC
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)

# Set up potentiometer on ADC pin 26
potentiometer = ADC(Pin(26))

# Colour variables
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0
turquoise = 0,128,128
purple = 255,0,255

# Define colour list
colours = [yellow, green, turquoise, blue, purple, red]

while True: # Run forever
    for j in colours:
        for i in range(15):
            # Set the next LED in the range to light with a colour
            strip[i] = (j)
            mydelay = potentiometer.read_u16()/50000
            
            time.sleep(mydelay)
            strip.write()