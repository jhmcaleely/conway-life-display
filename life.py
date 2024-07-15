# Python implementation of Conway's Life
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

import random


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
            state = world[line][col]
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

    n.append(world[line][(col-1) % col_c])
    n.append(world[line][(col+1) % col_c])

    n.extend(adjacent_line(world, world[(line + 1) % row_c], col))
    return n


def print_world(world):
    for line in range(len(world)):
        print(f'{line}: {world[line]}')
