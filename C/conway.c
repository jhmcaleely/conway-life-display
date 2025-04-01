/*
 * An implementation of Conway's Life
 */

#include "conway.h"
#include "cube_bit.h"

#include <stdlib.h>

static uint8_t random_state() {
    unsigned int half_way = (((unsigned int)RAND_MAX) + 1) / 2;
    return rand() < half_way ? 1 : 0;
}

void init_world(uint8_t* world, size_t count) {
    for (int i = 0; i < count; i++) {
        world[i] = random_state();
    }
}

static uint8_t neighbour_weight(uint8_t* world, uint8_t cell) {
    uint8_t count = 0;
    for (int i = 0; i < 8; i++) {
        uint8_t n = neighbour_of(cell, i);
        count += world[n];
    }
    return count;
}

static uint8_t next_state(uint8_t state, uint8_t alive_neighbours) {
    uint8_t new_state = 0;

    if (state == 1 && (alive_neighbours == 2 || alive_neighbours == 3)) {
        new_state = 1;
    }
    else if (state == 0 && alive_neighbours == 3) {
        new_state = 1;
    }
    return new_state;
}

void next_generation(uint8_t* current_world, uint8_t* next_world, size_t count) {
    for (int i = 0; i < count; i++) {
        uint8_t nw = neighbour_weight(current_world, i);
        next_world[i] = next_state(current_world[i], nw);
    }
}