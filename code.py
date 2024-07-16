# Conway's Life displayed on a 4tronix CUBE:BIT LED cube driven
# by a Pico:ed (a micro:bit pin compatible) board.
#
# We run two Life arrays, one on the 2D LED matrix on the
# Pico:ed, and one on the 3D matrix of the LED cube. The cube
# displays a 2D array wrapped around it's layers, rather than
# attempting to consider a 3D matrix for the Life game.

# Button A seeds the two Life arrays with random data
# Button B seeds the two Life arrays with one random live cell

import picoed
import time
import random

import life
import cubeled


def make_plane_world():
    return life.make_world(picoed.Display.width, picoed.Display.height)

# The 2D life array for the LED matrix on Pico:ed.
plane_world = make_plane_world()

def display_plane(world):
    # brigntess for the RED 
    liveLED = 50
    deadLED = 1

    for i in range(life.col_count(world)):
        for j in range(life.row_count(world)):
            pixel_bright = deadLED
            if life.get_cell(world, i, j) == life.live:
                pixel_bright = liveLED
            picoed.display.pixel(i, j, pixel_bright)
            

def make_cube_world():
    return life.make_world(cubeled.cube_side, cubeled.cube_side**2)

# The Life array for the CUBE:BIT Led Cube.
cube_world = make_cube_world()

def get_cube_cell(world, x, y, z):
    return life.get_cell(world, x, y+z*cubeled.cube_side)

def set_cube_cell(world, x, y, z, state):
    life.set_cell(world, x, y+z*cubeled.cube_side, state)


def display_cube(world):
    # two shades of red to mimic the Pico:ed LED matrix
    live = (128,0,0)
    dead = (16,0,0)

    for k in range(cubeled.cube_side):
        for j in range(cubeled.cube_side):
            for i in range(cubeled.cube_side):
                pixel_colour = dead
                if get_cube_cell(world, i, j, k) == life.live:
                    pixel_colour = live
                cubeled.set_pixel(i,j,k, pixel_colour)
    cubeled.cube_display_pixels.show()


def set_random_cell():
    i = random.randrange(life.col_count(plane_world))
    j = random.randrange(life.row_count(plane_world))
    life.set_cell(plane_world, i, j, life.live)
        
    i = random.randrange(cubeled.cube_side)
    j = random.randrange(cubeled.cube_side)
    k = random.randrange(cubeled.cube_side)
    set_cube_cell(cube_world, i, j, k, life.live)


while True:
    display_plane(plane_world)
    display_cube(cube_world)
    plane_world = life.next_generation(plane_world)
    cube_world = life.next_generation(cube_world)
    
    if picoed.button_a.is_pressed():
        # replace both worlds
        plane_world = make_plane_world()
        cube_world = make_cube_world()
        
    if picoed.button_b.is_pressed():
        set_random_cell()

    time.sleep(0.2)
    