import picoed
import life
import time
import random
import neopixel
import board

plane_live = 50
plane_dead = 1
plane_x = picoed.Display.width
plane_y = picoed.Display.height

plane_world = life.make_world(plane_x, plane_y)

def display_plane(world):
    for i in range(life.col_count(world)):
        for j in range(life.row_count(world)):
            pixel_colour = plane_dead
            if world[j][i] == life.live:
                pixel_colour = plane_live
            picoed.display.pixel(i, j, pixel_colour)
            
cube_side = 4

def make_cube_world(side):
    return life.make_world(cube_side, cube_side**2)

cube_world = make_cube_world(cube_side)

pixels = neopixel.NeoPixel(board.P0, cube_side**3, brightness=0.1, auto_write=False, pixel_order = neopixel.GRB)

# the LEDs are arranged serially, snaking around the cube.
cube_index = [ 0, 1, 2, 3, 7, 6, 5, 4, 8, 9,10,11,15,14,13,12,
              28,27,20,19,29,26,21,18,30,25,22,17,31,24,23,16,
              32,33,34,35,39,38,37,36,40,41,42,43,47,46,45,44,
              60,59,52,51,61,58,53,50,62,57,54,49,63,56,55,48
              ]

def cube_pixel(x, y, z, colour):
    global pixels
    pixels[cube_index[z*16+y*4+x]] = colour

def get_world_cube_pixel(world, x, y, z):
    return world[y+z*cube_side][x]

cube_live = (128,0,0)
cube_dead = (16,0,0)

def display_cube(world):
    for k in range(cube_side):
        for j in range(cube_side):
            for i in range(cube_side):
                pixel_colour = cube_dead
                if get_world_cube_pixel(world, i, j, k) == life.live:
                    pixel_colour = cube_live
                cube_pixel(i,j,k, pixel_colour)
    pixels.show()


while True:
    display_plane(plane_world)
    display_cube(cube_world)
    plane_world = life.next_generation(plane_world)
    cube_world = life.next_generation(cube_world)
    
    if picoed.button_a.is_pressed():
        plane_world = life.make_world(plane_x, plane_y)
        cube_world = life.make_world(cube_side, cube_side**2)
        
    if picoed.button_b.is_pressed():
        i = random.randrange(plane_x)
        j = random.randrange(plane_y)
        plane_world[j][i] = life.live
        
        i = random.randrange(cube_side)
        j = random.randrange(cube_side)
        k = random.randrange(cube_side)
        cube_world[j+k*cube_side][i] = life.live

    time.sleep(0.2)
    