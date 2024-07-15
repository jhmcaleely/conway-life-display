# a display for life patterns on the Cube:Bit

import life
import time
import neopixel
import board

side = 4

world = life.make_world(side**2, side)
life.print_world(world)

pixels = neopixel.NeoPixel(board.P0, 64, brightness=0.1, auto_write=False, pixel_order = neopixel.GRB)
pixels.fill((0,0,0))
pixels.show()

# the LEDs are arranged serially, snaking around the cube.
cube_index = [ 0, 1, 2, 3, 7, 6, 5, 4, 8, 9,10,11,15,14,13,12,
              28,27,20,19,29,26,21,18,30,25,22,17,31,24,23,16,
              32,33,34,35,39,38,37,36,40,41,42,43,47,46,45,44,
              60,59,52,51,61,58,53,50,62,57,54,49,63,56,55,48
              ]

def cube_pixel(x, y, z, colour):
    global cube_index, pixels
    pixels[cube_index[z*16+y*4+x]] = colour


live = (128,128,0)
dead = (0,0,64)

def display_world(world):
    for z in range(side):
        for j in range(side):
            for i in range(side):
                pixel_colour = dead
                if world[j+z*side][i] == life.live:
                    pixel_colour = live
                cube_pixel(i,j,z, pixel_colour)
    pixels.show()

display_world(world)
time.sleep(0.5)

while True:
    world = life.next_generation(world)
    life.print_world(world)
    display_world(world)
    time.sleep(0.5)

