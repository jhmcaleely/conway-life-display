# Conway's Life displayed on a 4tronix CUBE:BIT LED cube driven
# by a Raspberry Pi Pico.
#

import time
import random

import life
import cubeled



def make_cube_world():
    return life.make_world(56)

# The Life array for the CUBE:BIT Led Cube.
cube_world = make_cube_world()

def display_cube(world):

    live = (128,0,0)
    dead = (0,128,0)

    for k in range(len(cube_world)):
        pixel_colour = dead
        if cube_world[k] == life.live:
            pixel_colour = live
    
        cubeled.set_pixel(cubeled.led_index[k], pixel_colour)
    
    cubeled.cube_display_pixels.write()



while True:

    display_cube(cube_world)
    cube_world = life.next_generation(cube_world, cubeled.neighbourhoods)
    


    time.sleep(1)
    