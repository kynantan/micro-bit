from microbit import *

r = pin0
g = pin1
b = pin2

r_speed = 1
g_speed = 2
b_speed = 3

while True:
    redVal = ((running_time() // 100) * r_speed) % 255
    greenVal = ((running_time() // 100) * g_speed) % 255
    blueVal = ((running_time() // 100) * b_speed) % 255

    r.write_analog(1023 - (redVal * 4))
    g.write_analog(1023 - (greenVal * 4))
    b.write_analog(1023 - (blueVal * 4))

    sleep(200)
