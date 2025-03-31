#include <stdlib.h>

#include "pico/stdlib.h"
#include "ws2812.pio.h"


#define NUM_PIXELS 64
// limit brightness so that 2.5A USB power supply is sufficient.
#define PIXEL_MAX 128

// Match the GPIO from Raspberry Pi 40-Pin on 4Tronix Cube:BIT (GPIO18)
#define WS2812_GPIO 18

static inline void put_pixel(PIO pio, uint sm, uint32_t pixel_grb) {

    pio_sm_put_blocking(pio, sm, pixel_grb << 8u);
}

static inline uint32_t urgb_u32(uint8_t r, uint8_t g, uint8_t b) {
    return
            ((uint32_t) (r) << 8) |
            ((uint32_t) (g) << 16) |
            (uint32_t) (b);
}

uint32_t pixels[NUM_PIXELS];


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

    int i = 0;
    while (true) {
        pixels[i] = urgb_u32(64, 64, 64);

        for (int p = 0; p < NUM_PIXELS; p++) {
            put_pixel(pio, sm, pixels[p]);
        }

        sleep_ms(10);
        i += 1;

    }

    // This will free resources and unload our program
    pio_remove_program_and_unclaim_sm(&ws2812_program, pio, sm, offset);
}
