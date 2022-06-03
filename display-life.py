# a display for life patterns on the Cube:Bit

import life
import cubebit
import time

side = 4

cubebit.create(side)
cubebit.clear()
cubebit.show()
life.start()

live = cubebit.fromRGB(255,255,0)
dead = cubebit.fromRGB(128,0,0)

def display_world(world):
    for z in range(side):
        for i in range(side):
            for j in range(side):
                #print(z, i, j)
                if world[i+z*side][j] == life.dead:
                    cubebit.setPixel(cubebit.map(j,i,z), dead)
                else:
                    cubebit.setPixel(cubebit.map(j,i,z), live)
#            input("press a key")
    cubebit.show()

display_world(life.world)
time.sleep(2)

while True:
    life.tick()
    display_world(life.world)
    time.sleep(0.5)

