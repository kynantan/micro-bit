from microbit import *
import random

px = 2
py = 2

tx = random.randint(0, 4)
ty = random.randint(0, 4)

# this keeps track of the score
score = 0

while True:
    # if the score is less than our goal, play the game
    if score < 10:
        if px == tx:
            if py == ty:
                tx = random.randint(0, 4)
                ty = random.randint(0, 4)
                # make sure we add to our score
                score = score + 1
        x = accelerometer.get_x()
        if x > 50:
            if px < 4:
                px = px + 1
        elif x < -50:
            if px > 0:
                px = px - 1
        y = accelerometer.get_y()
        if y > 50:
            if py < 4:
                py = py + 1
        elif y < -50:
            if py > 0:
                py = py - 1
        display.clear()
        display.set_pixel(tx, ty, 4)
        display.set_pixel(px, py, 9)
        sleep(100)
    else:
        # if score is more than the goal, then show some text
        display.scroll("You win!")
