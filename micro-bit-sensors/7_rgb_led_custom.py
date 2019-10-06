from microbit import *
from random import randint

r = pin0
g = pin1
b = pin2

redVal = 65
greenVal = 224
blueVal = 224

while True:
    if button_a.is_pressed() is True and button_b.is_pressed() is True:
        r.write_analog(randint(0, 1023))
        g.write_analog(randint(0, 1023))
        b.write_analog(randint(0, 1023))
        sleep(500)
    else:
        r.write_analog(1023 - (redVal * 4))
        g.write_analog(1023 - (greenVal * 4))
        b.write_analog(1023 - (blueVal * 4))
        sleep(2000)
