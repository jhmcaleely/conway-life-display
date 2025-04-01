# Conway's Life displayed on a 4tronix CUBE:BIT LED cube driven
# by a Raspberry Pi Pico.

import time

import conway
import cube_bit

# The Life array for the CUBE:BIT Led Cube.
cube_world = conway.make_world(56)

def display_cube(world):

    live = (255,0,0)
    dead = (0,255,0)

    for k in range(len(cube_world)):
        pixel_colour = dead
        if cube_world[k] == conway.live:
            pixel_colour = live
    
        cube_bit.set_pixel(cube_bit.led_index[k], pixel_colour)
    
    cube_bit.cube_display_pixels.write()



while True:

    display_cube(cube_world)
    cube_world = conway.next_generation(cube_world)
    
    time.sleep(0.95)
    