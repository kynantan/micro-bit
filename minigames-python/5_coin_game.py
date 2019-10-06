from microbit import *
import random

# start the player in the centre
playerX = 2
playerY = 2

# start the coin at a random location
coinX = random.randint(0, 4)
coinY = random.randint(0, 4)

while True:
    # if the player collects the coin, move the coin to a random location
    if playerX == coinX:
        if playerY == coinY:
            coinX = random.randint(0, 4)
            coinY = random.randint(0, 4)
    
    # move the player on the x axis    
    x = accelerometer.get_x()
    if x > 50:
        if playerX < 4:
            playerX = playerX + 1
    elif x < -50:
        if playerX > 0:
            playerX = playerX - 1

    # move the player on the y axis    
    y = accelerometer.get_y()
    if y > 50:
        if playerY < 4:
            playerY = playerY + 1
    elif y < -50:
        if playerY > 0:
            playerY = playerY - 1
    
    # clear the display and then light up the current player and coin locations
    display.clear()
    display.set_pixel(coinX, coinY, 4)
    display.set_pixel(playerX, playerY, 9)
    
    # pause briefly so the code doesn't run too fast
    sleep(500)
