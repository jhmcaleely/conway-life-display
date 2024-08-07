# Python implementation of Conway's Life
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

# A 2D matrix of cells, which contain a running instance
# of Conway's Life.
#
# The neighbourhood (n) around a cell (c) is consulted to
# see if the cell should maintain or change state
#
#  nnn
#  ncn
#  nnn

import random

# characters handing for ascii state reports
live = '*'
dead = '-'

def random_state():
    if random.randrange(2) == 0:
        return dead
    else:
        return live

def make_row(cols):
    return [random_state() for _ in range(cols)]

def make_world(cols, lines):
    return [make_row(cols) for _ in range(lines)]

def row_count(world):
    return len(world)

def col_count(world):
    return len(world[0])

def get_cell(world, x, y):
    return world[y][x]

def set_cell(world, x, y, state):
    world[y][x] = state


def next_state(state, neighbourhood):
    new_state = dead
    alive_neighbours = neighbourhood.count(live)
    
    if state == live and (alive_neighbours == 2 or alive_neighbours == 3):
        new_state = live
    elif state == dead and alive_neighbours == 3:
        new_state = live

    return new_state


def next_generation(world):
    next_gen = []
    for line in range(row_count(world)):
        new_line = []
        for col in range(col_count(world)):
            neighbourhood = neighbours(world, line, col)
            state = get_cell(world, col, line)
            new_line.append(next_state(state, neighbourhood))

#            print(f'\
#({line}.{col}):{state}::{new_line[col]}:\
#({neighbourhood.count(live)},{neighbourhood})'
#                  )
        next_gen.append(new_line)

    return next_gen


def adjacent_line(world, line, col):
    return [line[(col + x) % col_count(world)] for x in range(-1, 2)]


def neighbours(world, line, col):
    n = []
    col_c = col_count(world)
    row_c = row_count(world)
    
    n.extend(adjacent_line(world, world[(line - 1) % row_c], col))

    n.append(get_cell(world, (col-1) % col_c, line))
    n.append(get_cell(world, (col+1) % col_c, line))

    n.extend(adjacent_line(world, world[(line + 1) % row_c], col))
    return n


def print_world(world):
    for line in range(len(world)):
        print(f'{line}: {world[line]}')
