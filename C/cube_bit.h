#ifndef cube_bit_h
#define cube_bit_h

#include <stdint.h>
#include <hardware/pio.h>

// Match the GPIO from Raspberry Pi 40-Pin on 4Tronix Cube:BIT (GPIO18)
#define WS2812_GPIO 18

#define SURFACE_LED_COUNT 56

extern uint8_t surface_leds[SURFACE_LED_COUNT];
extern uint8_t surface_neighbourhoods[SURFACE_LED_COUNT][8];

struct pixel {
    uint8_t r;
    uint8_t g;
    uint8_t b;
};

// 4x4 LED cube
#define NUM_PIXELS 64
extern struct pixel pixels[NUM_PIXELS];


void write_pixels(PIO pio, uint sm, struct pixel* pixels);

#endif