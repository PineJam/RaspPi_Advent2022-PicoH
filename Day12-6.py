import time
from machine import Pin
from neopixel import NeoPixel

button = Pin(15, Pin.IN, Pin.PULL_DOWN)
strip = NeoPixel(Pin(28), 15)

# Colour variables
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0
turquoise = 0,128,128
purple = 255,0,255

# Define colour list
colours = [yellow, turquoise, blue]

myindex = 0

# Variable with the number of items in our list (3)
# We -1 as the index starts a 0, and we want to use this for the colour list index number (0, 1 or 2)
# This is useful as it means we don't have to count the colours if we add more
indexlength = len(colours) -1

while True: # Run forever
    time.sleep(0.4) # Some delay
    if button() == 1:# If pressed
        # if the index variable <= length of the index
        if myindex < indexlength:
            # Add +1 to the index variable
            myindex = myindex + 1
        else:
            # Set index variable back to 0 (first item in our list)
            myindex = 0
        
        # Fill the strip with the current list index colour
        strip.fill((colours[myindex]))
        strip.write()