# Python implementation of Conway's Life
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

# A matrix of cells, which contain a running instance
# of Conway's Life.
#
# The neighbourhood (n) around a cell (c) is consulted to
# see if the cell should maintain or change state
#
#  nnn
#  ncn
#  nnn

import random
import cube_bit

live = 1
dead = 0


def random_state():
    if random.randrange(2) == 0:
        return dead
    else:
        return live


def make_world(size):
    return [random_state() for _ in range(size)]


def neighbour_weight(world, cell):
    count = 0
    for i in range(8):
        world_offset = cube_bit.neighbour_of(cell, i)
        count += world[world_offset]
    
    return count


def next_state(state, alive_neighbours):
    new_state = dead
    
    if state == live and (alive_neighbours == 2 or alive_neighbours == 3):
        new_state = live
    elif state == dead and alive_neighbours == 3:
        new_state = live

    return new_state


def next_generation(world):
    next_gen = []
    for cell in range(len(world)):
        nw = neighbour_weight(world, cell)
        next_gen.append(next_state(world[cell], nw))
    
    return next_gen