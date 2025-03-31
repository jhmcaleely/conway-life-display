# conway-life-display

[Conway's Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), on the [4tronix LED Cube](https://shop.4tronix.co.uk/products/cubebit), hosted on a [Pico:ed](https://www.elecfreaks.com/learn-en/pico-ed/index.html).

Tested on: Adafruit CircuitPython 9.1.0 on 2024-07-10; ELECFREAKS PICO:ED with rp2040

Displays two life games, one on the LED cube, and one on the LED matrix on the pico:ed

## 4tronix CUBE:BIT

The CUBE:BIT: https://shop.4tronix.co.uk/products/cubebit

This LED cube is a string of WS2812 compatible LEDs, arranged as two apparently parallel strings. A 4x4 cube has 128 LEDs, at 64 addressable positions.

The board wires them with three wires: Power (5V, GND) and Data ('DIN').

The addressable positions in each plane, from bottom (0) to top (3) follow one of two orientations (A or B). The orientations alternate as the planes stack.

```
Plane 0 (Orientation A): (bottom)
 15  14  13  12
  8   9  10  11
  7   6   5   4
  0   1   2   3

Plane 1 (Orientation B):
 31  24  23  16
 30  25  22  17
 29  26  21  18
 28  27  20  19

Plane 2 (Orientation A):
 47  46  45  44
 40  41  42  43
 39  38  37  36
 32  33  34  35

Plane 3 (Orientation B):
 63  56  55  48
 62  57  54  49
 61  58  53  50
 60  59  52  51
```

### Cube:Base layout

```
               40-Pin
               https://pinout.xyz
               1                   39
               2    12             40
              -----------+------------
 DC (5V, 5A) + Plane 0:               |
             |     15  14  13  12     | 0
 Jumpers     +      8   9  10  11     | |  Micro:Bit
             |      7   6   5   4     | |  https://microbit.pinout.xyz
  Micro-USB  +      0   1   2   3     | GND
             |                        |
              -+-------+----------+---
              GVS  Playground  Crumble
```

The LEDs have 'DIN' (data) wired to pin 12 (GPIO 18) on the 40-bit, and Pin 0 on the Micro:Bit. In both cases the base supplies power to the attached board. 3v for the Micro:Bit, and 5V for the 40-Pin.

### Current Consumption

Blogs (eg https://www.electromaker.io/blog/article/building-a-cube-with-cubebit?srsltid=AfmBOoqWBwbmUz-08ZEl8w9UU0P54sTTHbSFe7JiEvFA-ux9oO65n4U2) cite a 4tronix table of consumption that I can't directly source:

| Size | Description | Current |
| ---- | ----------- | ------- |
| 4x4x4 | all LEDs at Red, brightness 40 | 350mA |
| 4x4x4 | all LEDs at White, brightness 40 | 800mA |
| 4x4x4 | all LEDs at White, brightness 255 | 4.5A |

Source code elsewhere suggests keeping brightness to less than white 127 if you want to power the cube from a 2.5A USB source.
