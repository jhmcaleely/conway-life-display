from picoed import *
import life
import time
import random
import neopixel
import board

live = 20
dead = 0

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

for k in range(4):
    for j in range(4):
        for i in range(4):
            cube_pixel(i,j,k,(0,255,0))
            pixels.show()
            time.sleep(0.1)
    

world = life.make_world(7, 17)
#life.print_world(world)

def display_world(world):
    for i in range(17):
        for j in range(7):
            pixel_colour = dead
            if world[j][i] == life.live:
                pixel_colour = live
            display.pixel(i, j, pixel_colour)

while True:
    display_world(world)
    world = life.next_generation(world)
    if button_a.is_pressed():
        world = life.make_world(7, 17)
    if button_b.is_pressed():
        i = random.randrange(7)
        j = random.randrange(17)
        world[i][j] = life.live
    time.sleep(0.2)