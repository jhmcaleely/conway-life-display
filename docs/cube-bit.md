# 4tronix CUBE:BIT

The CUBE:BIT: https://shop.4tronix.co.uk/products/cubebit

This is a flexible LED cube design, intended to be driven by a 40-pin Raspberry Pi (A Pi Zero can be directly mounted) or a Micro:Bit.

The LED cube is a string of WS2812 compatible LEDs, arranged as two apparently parallel strings. A 4x4 cube has 128 LEDs, at 64 addressable positions.

The board connects them with three wires: Power (5V, GND) and Data ('DIN').

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

## Cube:Base layout

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

The LEDs have 'DIN' (data) wired to pin 12 (GPIO 18) on the 40-bit, and Pin 0 on the Micro:Bit. In both cases the base supplies power to the attached board (3v for the Micro:Bit, and 5v for the 40-Pin attached Pi).

Power can be supplied by a micro-usb supply (eg, a [2.5A Raspberry Pi supply](https://www.raspberrypi.com/products/micro-usb-power-supply/)), the 'Crumble' pads, the headers labelled GVS or the DC barrel jack. The DC barrel socket is suitable for a standard 2.1mm centre positive barrel jack. The Jumpers select which source the board uses for power. Any suspply less than 5A in capacity will require the software to limit the led brightness to less than the maximum.

## Current Consumption

Several blogs (eg [ElectroMaker](https://www.electromaker.io/blog/article/building-a-cube-with-cubebit?srsltid=AfmBOoqWBwbmUz-08ZEl8w9UU0P54sTTHbSFe7JiEvFA-ux9oO65n4U2) ) cite a 4tronix table of consumption that I can't directly source:

| Size | Description | Current |
| ---- | ----------- | ------- |
| 4x4x4 | all LEDs at Red, brightness 40 | 350mA |
| 4x4x4 | all LEDs at White, brightness 40 | 800mA |
| 4x4x4 | all LEDs at White, brightness 255 | 4.5A |

These are broadly matched by my own measurements on the board I have. If you use a 2.5A USB source, you can limit the maximum brightness to 127 (50%), and not draw too much current. My own board draws around 2.1A when showing white at 50% brightness.
