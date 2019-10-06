from microbit import *

# control an RGB LED with common anode

r = pin0
g = pin1
b = pin2

while True:

    # red
    r.write_digital(0)
    g.write_digital(1)
    b.write_digital(1)

    sleep(1000)

    # green
    r.write_digital(1)
    g.write_digital(0)
    b.write_digital(1)

    sleep(1000)

    # blue
    r.write_digital(1)
    g.write_digital(1)
    b.write_digital(0)

    sleep(1000)
