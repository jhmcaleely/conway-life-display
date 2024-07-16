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
import life
import time
import random
import neopixel
import board


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
            
cube_side = 4

def make_cube_world():
    return life.make_world(cube_side, cube_side**2)

# The Life array for the CUBE:BIT Led Cube.
cube_world = make_cube_world()

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

def set_cube_pixel(x, y, z, colour):
    global cube_display_pixels
    cube_display_pixels[cube_index[z*16+y*4+x]] = colour

def get_cube_cell(world, x, y, z):
    return life.get_cell(world, x, y+z*cube_side)

def set_cube_cell(world, x, y, z, state):
    life.set_cell(world, x, y+z*cube_side, state)


def display_cube(world):
    # two shades of red to mimic the Pico:ed LED matrix
    live = (128,0,0)
    dead = (16,0,0)

    for k in range(cube_side):
        for j in range(cube_side):
            for i in range(cube_side):
                pixel_colour = dead
                if get_cube_cell(world, i, j, k) == life.live:
                    pixel_colour = live
                set_cube_pixel(i,j,k, pixel_colour)
    cube_display_pixels.show()


def set_random_cell():
    i = random.randrange(life.col_count(plane_world))
    j = random.randrange(life.row_count(plane_world))
    life.set_cell(plane_world, i, j, life.live)
        
    i = random.randrange(cube_side)
    j = random.randrange(cube_side)
    k = random.randrange(cube_side)
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
    