# Python implementation of Conway's Life
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life


map = []

col_d = 4
line_d = 8

live = '*'
dead = '-'

import random

def make_node():
    state = random.randrange(2)
    if state == 0:
        return dead
    else:
        return live

def make_row():
    row = []
    for node in range(col_d):
        row.append(make_node())
    return row

def make_map():
    fresh_map = []
    for line in range(line_d):
        fresh_map.append(make_row())
    return fresh_map


def next_state(line, col):
    neighbourhood = neighbours(line, col)
    state = map[line][col]

    new_state = dead
    alive_neighbours = neighbourhood.count(live)
    if state == live and (alive_neighbours == 2 or alive_neighbours == 3):
        new_state = live
    elif state == dead and alive_neighbours == 3:
        new_state = live
    return new_state


def next_generation():
    next_gen = map.copy()
    for line in range(len(map)):
        for col in range(len(map[line])):
            next_gen[line][col] = next_state(line, col)
    return next_gen



def n_line(line, col):
    n = []
    n.append(map[line][(col-1) % col_d])
    n.append(map[line][col])
    n.append(map[line][(col+1) % col_d])
    return n


def neighbours(line, col):
    n = []
    n.extend(n_line((line - 1) % line_d, col))
    n.append(map[line][(col-1) % col_d])
    n.append(map[line][(col+1) % col_d])
    n.extend(n_line((line + 1) % line_d, col))
    return n

def print_neighbours(n):
    print(f'{n[:3]}')
    print(f'{n[3:4]} x {n[4:5]}')
    print(f'{n[5:]}')


def print_map(map):
    for line in range(len(map)):
        print(f'{line}: {map[line]}')


map = make_map()
print_map(map)
map = next_generation()
print_map(map)
