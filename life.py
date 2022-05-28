# Python implementation of Conway's Life
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

print('hello world')

map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

new_map = map.copy()

for line in range(len(map)):
    for col in range(len(map[line])):
        new_map[line][col] = (line, col)

col_d = len(map[0])
line_d = len(map)

def n_line(line, col):
    n = []
    n.append(map[line][(col-1) % col_d])
    n.append(map[line][col])
    n.append(map[line][(col+1) % col_d])
    return n


def neighbours(line, col):
    n = []
    n.append(n_line((line - 1) % line_d, col))
    n.append(map[line][(col-1) % col_d])
    n.append(map[line][(col+1) % col_d])
    n.append(n_line((line + 1) % line_d, col))
    return n