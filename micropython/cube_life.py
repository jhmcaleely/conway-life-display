# Conway's Life displayed on a 4tronix CUBE:BIT LED cube driven
# by a Raspberry Pi Pico.

import time

import conway
import cube_bit

# The Life array for the CUBE:BIT Led Cube.
surface_world = conway.make_world(56)

def display_on_surface(world):

    live = (255,0,0)
    dead = (0,255,0)

    for k in range(len(world)):
        pixel_colour = dead
        if world[k] == conway.live:
            pixel_colour = live
    
        cube_bit.set_pixel(cube_bit.surface_leds[k], pixel_colour)
    
    cube_bit.cube_display_pixels.write()

def surface_neighbour_of(cell, neighbour):
    led = cube_bit.surface_neighbourhoods[cell][neighbour]
    return cube_bit.surface_leds.index(led)


while True:
    display_on_surface(surface_world)
    surface_world = conway.next_generation(surface_world, surface_neighbour_of)
    
    time.sleep(0.95)
    