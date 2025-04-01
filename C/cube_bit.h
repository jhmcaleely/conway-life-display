#ifndef cube_bit_h
#define cube_bit_h

#include <stdint.h>
#include <hardware/pio.h>

// Match the GPIO from Raspberry Pi 40-Pin on 4Tronix Cube:BIT (GPIO18)
#define WS2812_GPIO 18

// 4x4 LED cube
#define NUM_PIXELS 64

// limit brightness so that 2.5A USB power supply is sufficient.
#define PIXEL_MAX (((UINT8_MAX + 1) / 2) - 1)

struct pixel {
    uint8_t r;
    uint8_t g;
    uint8_t b;
};

extern struct pixel pixels[NUM_PIXELS];
extern uint8_t led_index[56];

void write_pixels(PIO pio, uint sm, struct pixel* pixels);
uint8_t neighbour_of(uint8_t cell, uint8_t neighbour);

#endif