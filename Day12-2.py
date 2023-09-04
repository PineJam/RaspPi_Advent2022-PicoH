# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Select the first pixel (pixel 0)
# Set the RGB colour (my turquoise colour)
# iterate over 15 leds
for i in range(15):
    if i > 7:
        # Fill the strip with my turquoise colour
        strip[i] = (0,128,128)
    else:
        # Fill the strip with Raspberry interpretation turquoise
        strip[i] = (72,209,204)

# Send the data to the strip
strip.write()
time.sleep(10)

# Switch off leds
strip.fill((0,0,0))
strip.write()




