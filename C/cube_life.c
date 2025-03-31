/*
 * Conway's Life on the 4Tronix Cube:BIT, C/Pico edition.
 */
#include <stdlib.h>
#include <stdint.h>

#include "pico/stdlib.h"
#include "ws2812.pio.h"

// Match the GPIO from Raspberry Pi 40-Pin on 4Tronix Cube:BIT (GPIO18)
#define WS2812_GPIO 18

// 4x4 LED cube
#define NUM_PIXELS 64

// limit brightness so that 2.5A USB power supply is sufficient.
#define PIXEL_MAX (UINT8_MAX / 2)

static uint8_t clamp_brightness(uint8_t raw) {
    if (PIXEL_MAX < UINT8_MAX) {
        uint8_t divider = UINT8_MAX / PIXEL_MAX;
        return raw / divider;
    } else {
        return raw;
    }
}

struct pixel {
    uint8_t r;
    uint8_t g;
    uint8_t b;
};

struct pixel pixels[NUM_PIXELS];

static void write_pixels(PIO pio, uint sm, struct pixel* pixels) {
    for (int i = 0; i < NUM_PIXELS; i++) {

        struct pixel p;
        p.r = clamp_brightness(pixels[i].r);
        p.g = clamp_brightness(pixels[i].g);
        p.b = clamp_brightness(pixels[i].b);
        
        // pack the pixel into the top 24 bits of a 32bit word for transport to the pio state machine.
        uint32_t pixel = ((uint32_t) p.r) << 16 | 
                         ((uint32_t) p.g) << 24 | 
                         ((uint32_t) p.b) << 8;

        pio_sm_put_blocking(pio, sm, pixel);

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

    int i = 0;
    while (true) {
        pixels[i].r = UINT8_MAX;
        pixels[i].g = UINT8_MAX;
        pixels[i].b = UINT8_MAX;

        write_pixels(pio, sm, pixels);

        sleep_ms(10);
        i += 1;

    }
}
