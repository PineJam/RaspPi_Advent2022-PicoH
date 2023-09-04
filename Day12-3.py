# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip in number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28),15)

# Colour variables
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0
turquoise = 0,128,128
pink = 255,20,147

# iterate over 15 LEDs
j=1
for i in range(15):
    if j == 1:
        strip[i] = (pink)
        j = j+1
    elif j == 2:
        strip[i] = (turquoise)
        j = j+1
    elif j == 3:
        strip[i] = (yellow)
        j = 1

strip.write()
time.sleep(15)
strip.fill((0,0,0))
strip.write()