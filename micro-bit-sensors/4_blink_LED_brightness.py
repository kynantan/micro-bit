from microbit import *

brightness = 500

while True:

    a_presses = button_a.get_presses()
    brightness = brightness - (a_presses * 50)
    if brightness < 0:
        brightness = 0

    b_presses = button_b.get_presses()
    brightness = brightness + (b_presses * 50)
    if brightness > 1000:
        brightness = 1000

    pin0.write_analog(0)
    sleep(200)
    pin0.write_analog(brightness)
    sleep(200)
