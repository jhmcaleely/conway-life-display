# Python implementation of Conway's Life
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life


world = []

col_d = 4
line_d = 16

live = '*'
dead = '-'

import random

def random_state():
    if random.randrange(2) == 0:
        return dead
    else:
        return live


def make_row(cols=col_d):
    return [random_state() for _ in range(cols)]


def make_world(lines=line_d, cols=col_d):
    return [make_row(cols) for _ in range(lines)]


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
    for line in range(len(world)):
        new_line = []
        for col in range(len(world[line])):
            neighbourhood = neighbours(world, line, col)
            state = world[line][col]
            new_line.append(next_state(state, neighbourhood))

            print(f'\
({line}.{col}):{state}::{new_line[col]}:\
({neighbourhood.count(live)},{neighbourhood})'
                  )
        next_gen.append(new_line)

    return next_gen


def adjacent_line(line, col):
    return [line[(col + x) % col_d] for x in range(-1, 2)]


def neighbours(world, line, col):
    n = []
    n.extend(adjacent_line(world[(line - 1) % line_d], col))

    n.append(world[line][(col-1) % col_d])
    n.append(world[line][(col+1) % col_d])

    n.extend(adjacent_line(world[(line + 1) % line_d], col))
    return n


def print_neighbours(n):
    print(f'{n[:3]}')
    print(f'{n[3:4]} x {n[4:5]}')
    print(f'{n[5:]}')


def print_world(world):
    for line in range(len(world)):
        print(f'{line}: {world[line]}')


def tick():
    global world
    world = next_generation(world)
    print_world(world)


def start():
    global world
    world = make_world()
    print_world(world)


start()
tick()
tick()
