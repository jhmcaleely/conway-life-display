/*
 * Conway's Life on the 4Tronix Cube:BIT, C/Pico edition.
 */
#include <stdlib.h>
#include <stdint.h>

#include <pico/stdlib.h>
#include "ws2812.pio.h"

#include "conway.h"
#include "cube_bit.h"

#define WORLD_SIZE SURFACE_LED_COUNT

uint8_t world_storage[2][WORLD_SIZE];

uint8_t* current_world = &world_storage[1][0];
uint8_t* new_world = &world_storage[0][0];

void display_on_surface(PIO pio, uint sm, uint8_t* world, size_t count) {
    for (int c = 0; c < count; c++) {
        if (world[c] == 0) {
            pixels[surface_leds[c]].r = UINT8_MAX;
            pixels[surface_leds[c]].g = 0;
            pixels[surface_leds[c]].b = 0;
        } else {
            pixels[surface_leds[c]].r = 0;
            pixels[surface_leds[c]].g = UINT8_MAX;
            pixels[surface_leds[c]].b = 0;
        }
    }

    write_pixels(pio, sm, pixels);
}

uint8_t surface_neighbour_of(uint8_t cell, uint8_t neighbour) {
    uint8_t led = surface_neighbourhoods[cell][neighbour];
    for (int i = 0; i < SURFACE_LED_COUNT; i++) {
        if (surface_leds[i] == led) {
            return i;
        }
    }
}


int main() {
    set_sys_clock_48mhz();
    stdio_init_all();

    // todo get free sm
    PIO pio;
    uint sm;
    uint offset;

    // This will find a free pio and state machine for our program and load it for us
    bool success = pio_claim_free_sm_and_add_program(&ws2812_program, &pio, &sm, &offset);
    hard_assert(success);

    ws2812_program_init(pio, sm, offset, WS2812_GPIO, 800000);

    init_world(current_world, WORLD_SIZE);

    while (true) {

        display_on_surface(pio, sm, current_world, WORLD_SIZE);
        next_generation(current_world, new_world, WORLD_SIZE, surface_neighbour_of);

        uint8_t* temp = current_world;
        current_world = new_world;
        new_world = temp;

        sleep_ms(950);
    }
}
