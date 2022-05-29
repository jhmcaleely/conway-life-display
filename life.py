# Python implementation of Conway's Life
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life


map = []

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


def make_map(lines=line_d, cols=col_d):
    return [make_row(cols) for _ in range(lines)]


def next_state(state, neighbourhood):
    new_state = dead
    alive_neighbours = neighbourhood.count(live)
    
    if state == live and (alive_neighbours == 2 or alive_neighbours == 3):
        new_state = live
    elif state == dead and alive_neighbours == 3:
        new_state = live

    return new_state


def next_generation(map):
    next_gen = []
    for line in range(len(map)):
        new_line = []
        for col in range(len(map[line])):
            neighbourhood = neighbours(map, line, col)
            state = map[line][col]
            new_line.append(next_state(state, neighbourhood))

            print(f'\
({line}.{col}):{state}::{new_line[col]}:\
({neighbourhood.count(live)},{neighbourhood})'
                  )
        next_gen.append(new_line)

    return next_gen


def adjacent_line(line, col):
    return [line[(col + x) % col_d] for x in range(-1, 2)]


def neighbours(map, line, col):
    n = []
    n.extend(adjacent_line(map[(line - 1) % line_d], col))

    n.append(map[line][(col-1) % col_d])
    n.append(map[line][(col+1) % col_d])

    n.extend(adjacent_line(map[(line + 1) % line_d], col))
    return n


def print_neighbours(n):
    print(f'{n[:3]}')
    print(f'{n[3:4]} x {n[4:5]}')
    print(f'{n[5:]}')


def print_map(map):
    for line in range(len(map)):
        print(f'{line}: {map[line]}')


def tick():
    global map
    map = next_generation(map)
    print_map(map)


def start():
    global map
    map = make_map()
    print_map(map)


start()
tick()
tick()
