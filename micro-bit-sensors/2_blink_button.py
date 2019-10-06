from microbit import *

brightness = 9

while True:
    if button_a.is_pressed() is True:
        display.set_pixel(0, 0, brightness)
        sleep(50)
        display.clear()
        sleep(50)
    else:    
        display.set_pixel(0, 0, brightness)
        sleep(1000)
        display.clear()
        sleep(1000)
