# a display for life patterns on the Cube:Bit

import life
import cubebit
import time

side = 4

world = life.make_world(side**2, side)
life.print_world(world)

cubebit.create(side)
cubebit.clear()
cubebit.show()
time.sleep(0.5)

live = cubebit.fromRGB(128,128,0)
dead = cubebit.fromRGB(0,0,64)

def display_world(world):
    for z in range(side):
        for i in range(side):
            for j in range(side):
                pixel_colour = dead
                if world[i+z*side][j] == life.live:
                    pixel_colour = live
                cubebit.setPixel(cubebit.map(j,i,z), pixel_colour)
    cubebit.show()

display_world(world)
time.sleep(0.5)

while True:
    world = life.next_generation(world)
    life.print_world(world)
    display_world(world)
    time.sleep(0.5)

