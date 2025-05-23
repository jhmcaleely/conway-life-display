# The CUBE:BIT LED Cube is a string of 'neopixels' (serial multi-colour
# LEDs) that are arranged off of pin 0 of the Pico:ed connector.

import neopixel, machine

max_brightness = 127

# CUBE:BIT has GRB Leds, on an 800MHz capable bus.
cube_display_pixels = neopixel.NeoPixel(machine.Pin(18), 64, 3, 1)


# the leds that are on the surface of the cube.
surface_leds = [  0,  1,  2,  3,  4,  5,  6,  7, 
               8,  9, 10, 11, 12, 13, 14, 15,
              16, 17, 18, 19, 20,         23,
              24,         27, 28, 29, 30, 31,
              32, 33, 34, 35, 36,         39,
              40,         43, 44, 45, 46, 47,
              48, 49, 50, 51, 52, 53, 54, 55,
              56, 57, 58, 59, 60, 61, 62, 63]


# a topological map of the neighbours for each surface led.
surface_neighbourhoods = [ [  7,  6,  1,  7,  1, 29, 28, 27 ],  # Led: 0 (corner)
                   [  7,  6,  5,  0,  2, 28, 27, 20 ],
                   [  6,  5,  4,  1,  3, 27, 20, 19 ],
                   [  2,  5,  4,  2,  4, 20, 19, 18 ],  # Led: 3 (corner)
                   [  2,  5, 10,  3, 11, 19, 18, 17 ],
                   [  1,  6,  9,  2, 10,  3,  4, 11 ],
                   [  0,  7,  8,  1,  9,  2,  5, 10 ],
                   [ 28, 29, 30,  0,  8,  1,  6,  9 ],  # Led: 7
                   [  6,  9, 14,  7, 15, 29, 30, 31 ],
                   [  7,  8, 15,  6, 14,  5, 10, 13 ],
                   [  6,  9, 14,  5, 13,  4, 11, 12 ],
                   [  5, 10, 13,  4, 12, 18, 17, 16 ],
                   [ 11, 10, 13, 11, 13, 17, 16, 23 ],  # Led: 12 (corner)
                   [  9, 14, 24, 10, 23, 11, 12, 16 ],
                   [  8, 15, 31,  9, 24, 10, 13, 23 ],
                   [  8,  9, 14,  8, 14, 30, 31, 24 ],  # Led: 15 (corner)
                   [ 11, 12, 13, 17, 23, 43, 44, 45 ],
                   [  4, 11, 12, 18, 16, 36, 43, 44 ],
                   [  3,  4, 11, 19, 17, 35, 36, 43 ],
                   [  2,  3,  4, 20, 18, 34, 35, 36 ],
                   [  1,  2,  3, 27, 19, 33, 34, 35 ],

    
                   [ 14, 13, 12, 24, 16, 46, 45, 44 ], # Led: 23
                   [ 15, 14, 13, 31, 23, 47, 46, 45 ],

    
                   [  0,  1,  2, 28, 20, 32, 33, 34 ],
                   [  7,  0,  1, 29, 27, 39, 32, 33 ],
                   [  8,  7,  0, 30, 28, 40, 39, 32 ],
                   [ 15,  8,  7, 31, 29, 47, 40, 39 ],
                   [ 14, 15,  8, 24, 30, 46, 47, 40 ],  # Led: 31
                   [ 29, 28, 27, 39, 33, 61, 60, 59 ],
                   [ 28, 27, 20, 32, 34, 60, 59, 52 ],
                   [ 27, 20, 19, 33, 35, 59, 52, 51 ],
                   [ 20, 19, 18, 34, 36, 52, 51, 50 ],
                   [ 49, 50, 51, 43, 35, 17, 18, 19 ],

    
                   [ 30, 29, 28, 40, 32, 62, 61, 60 ],  # Led: 39
                   [ 29, 30, 31, 47, 39, 63, 62, 61 ],

    
                   [ 48, 49, 50, 44, 36, 16, 17, 18 ],
                   [ 55, 48, 49, 45, 43, 23, 16, 17 ],
                   [ 24, 23, 16, 46, 44, 56, 55, 48 ],
                   [ 31, 24, 23, 47, 45, 63, 56, 55 ],
                   [ 30, 31, 24, 40, 46, 62, 63, 56 ],  # Led: 47
                   [ 45, 44, 43, 55, 49, 55, 54, 49 ],  # Led: 48 (corner)
                   [ 55, 48, 44, 54, 43, 53, 50, 36 ],
                   [ 54, 49, 43, 53, 36, 52, 51, 35 ],
                   [ 36, 35, 34, 50, 52, 50, 53, 52 ],  # Led: 51 (corner)
                   [ 58, 53, 50, 59, 51, 33, 34, 35 ], 
                   [ 57, 54, 49, 58, 50, 59, 52, 51 ],
                   [ 56, 55, 48, 57, 49, 58, 53, 50 ],
                   [ 46, 45, 44, 56, 48, 57, 54, 49 ],  # Led: 55
                   [ 47, 46, 45, 63, 55, 62, 57, 54 ],
                   [ 63, 56, 55, 62, 54, 61, 58, 53 ],
                   [ 62, 57, 54, 61, 53, 60, 59, 52 ],
                   [ 61, 58, 53, 60, 52, 32, 33, 34 ],
                   [ 39, 32, 33, 61, 59, 61, 58, 59 ],  # Led: 60 (corner)
                   [ 40, 39, 32, 62, 60, 57, 58, 59 ],
                   [ 47, 40, 39, 63, 61, 56, 57, 58 ],
                   [ 40, 47, 46, 62, 56, 62, 57, 56 ] ] # Led: 63 (corner)


def clamp_brightness(channel):
    if (max_brightness < 255):
        divider = 256 // (max_brightness + 1)
        return channel // divider
    else:
        return channel


def set_pixel(k, colour):
    r, g, b = colour
    clamped = (clamp_brightness(r), clamp_brightness(g), clamp_brightness(b))

    cube_display_pixels[k] = clamped
    

def write_pixels():
    cube_display_pixels.write()