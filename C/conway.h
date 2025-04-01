#ifndef conway_h
#define conway_h

#include <stddef.h>
#include <stdint.h>

extern uint8_t led_index[56];

void init_world(uint8_t* world, size_t count);
void next_generation(uint8_t* current_world, uint8_t* next_world, size_t count);

#endif