import board
import neopixel
#pixels = neopixel.NeoPixel(board.D18, 192)
pixels = neopixel.NeoPixel(board.D10, 6)
pixels[1] = (255, 0, 0)
#pixels.fill((0, 0, 0))