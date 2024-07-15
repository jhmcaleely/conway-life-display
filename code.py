from picoed import *
import life
import time
import random
import neopixel
import board

plane_live = 20
plane_dead = 0
plane_x = 17
plane_y = 7

plane_world = life.make_world(plane_x, plane_y)

def display_plane(world):
    for i in range(life.col_count(world)):
        for j in range(life.row_count(world)):
            pixel_colour = plane_dead
            if world[j][i] == life.live:
                pixel_colour = plane_live
            display.pixel(i, j, pixel_colour)
            
cube_side = 4

cube_world = life.make_world(cube_side, cube_side**2)

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

cube_live = (128,128,0)
cube_dead = (0,0,64)

def display_cube(world):
    for z in range(cube_side):
        for j in range(cube_side):
            for i in range(cube_side):
                pixel_colour = cube_dead
                if world[j+z*cube_side][i] == life.live:
                    pixel_colour = cube_live
                cube_pixel(i,j,z, pixel_colour)
    pixels.show()


while True:
    display_plane(plane_world)
    display_cube(cube_world)
    plane_world = life.next_generation(plane_world)
    cube_world = life.next_generation(cube_world)
    
    if button_a.is_pressed():
        plane_world = life.make_world(plane_x, plane_y)
        cube_world = life.make_world(cube_side, cube_side**2)
        
    if button_b.is_pressed():
        i = random.randrange(plane_x)
        j = random.randrange(plane_y)
        plane_world[j][i] = life.live
        
        i = random.randrange(cube_side)
        j = random.randrange(cube_side)
        k = random.randrange(cube_side)
        cube_world[j+k*cube_side][i] = life.live

    time.sleep(0.2)
    