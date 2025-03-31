# The CUBE:BIT LED Cube is a string of 'neopixels' (serial multi-colour
# LEDs) that are arranged off of pin 0 of the Pico:ed connector.

import neopixel
import board

cube_side = 4

# Pico:ed is connected to the 'neopixel' string via Micro:Bit
# pin 0. CUBE:BIT has GRB Leds.
cube_display_pixels = neopixel.NeoPixel(board.P0,
                                        cube_side**3,
                                        # avoid brightness over 40% to stay within USB
                                        # power budget.
                                        brightness=0.1,
                                        auto_write=False,
                                        pixel_order = neopixel.GRB)

# the LEDs are arranged serially, snaking around the cube.
cube_index = [ 0, 1, 2, 3, 7, 6, 5, 4, 8, 9,10,11,15,14,13,12,
              28,27,20,19,29,26,21,18,30,25,22,17,31,24,23,16,
              32,33,34,35,39,38,37,36,40,41,42,43,47,46,45,44,
              60,59,52,51,61,58,53,50,62,57,54,49,63,56,55,48
              ]

def set_pixel(x, y, z, colour):
    global cube_display_pixels
    cube_display_pixels[cube_index[z*16+y*4+x]] = colour