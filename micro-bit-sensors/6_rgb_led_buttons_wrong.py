from microbit import *
from random import randint

r = pin0
g = pin1
b = pin2

while True:
    if button_a.is_pressed() is True:
        r.write_digital(0)
        g.write_digital(1)
        b.write_digital(0)
    elif button_b.is_pressed() is True:
        r.write_digital(0)
        g.write_digital(0)
        b.write_digital(1)
    else:
        r.write_digital(1)
        g.write_digital(0)
        b.write_digital(0)
