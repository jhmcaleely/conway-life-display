/*
 * Conway's Life on the 4Tronix Cube:BIT, C/Pico edition.
 */
#include <stdlib.h>
#include <stdint.h>

#include "pico/stdlib.h"
#include "ws2812.pio.h"

#include "conway.h"
#include "cube_bit.h"




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

    uint8_t worldA[56];
    uint8_t worldB[56];

    uint8_t* current_world = &worldA[0];
    uint8_t* new_world = &worldB[0];

    init_world(current_world, 56);

    while (true) {

        for (int c = 0; c < 56; c++) {
            if (current_world[c] == 0) {
                pixels[led_index[c]].r = UINT8_MAX;
                pixels[led_index[c]].g = 0;
                pixels[led_index[c]].b = 0;
            } else {
                pixels[led_index[c]].r = 0;
                pixels[led_index[c]].g = UINT8_MAX;
                pixels[led_index[c]].b = 0;
            }
        }

        write_pixels(pio, sm, pixels);

        sleep_ms(950);
        next_generation(current_world, new_world, 56);

        uint8_t* temp = current_world;
        current_world = new_world;
        new_world = temp;

    }
}
