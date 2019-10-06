from microbit import *

brightness = 9

while True:
    display.set_pixel(0, 0, brightness)
    sleep(1000)
    display.clear()
    sleep(1000)
