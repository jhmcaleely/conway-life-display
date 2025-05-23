# conway-life-display

Conway's Life implemented on a LED cube, hosted on a Raspberry Pi Pico.

![An LED cube, with a Pico based daughterboard. Displaying red and green illuminated leds.](docs/conway-life-display.jpeg)

Some [reverse engineered notes](docs/cube-bit.md) of the [4tronix LED Cube](https://shop.4tronix.co.uk/products/cubebit).

Implemented in C and Micropython. Either implementation can be run as firmware on the Pico.

## Hardware

`cube-bit/`

contains a kicad project that connects a pico to the 40-pin Pi connector.

`Plinth/`

contains a lightburn project to create a plinth for the Cube:Bit + Pico to sit on. Originally drawn using [Boxes.py](https://boxes.hackerspace-bamberg.de/?language=en). 
