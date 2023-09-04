# Imports
import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(28),15)

# Colour variables
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0
turquoise = 0,128,128
purple = 128,0,128

# Define colour list
colours = [yellow, green, turquoise, blue, purple, red]

while True:
    for j in colours:
        for i in range(15):
            strip[i] = (j)
            time.sleep(0.1)
            strip.write()