import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)
delay = 0.01 # fade speed

while True:
    for i in range (1,128,1): # iterate from 1 - 255 in steps of 1
        strip.fill((0,i,i))
        strip.write()
        time.sleep(delay)
    
    for i in range (128,1,-1):
        strip.fill((0,i,i))
        strip.write()
        time.sleep(delay)