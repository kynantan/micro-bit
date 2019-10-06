from microbit import *

time = 1000

angle = 0
pin0.write_analog(angle)
sleep(time)

while True:
    
    if button_a.was_pressed():
        if angle < 100:
            angle = angle + 10
            print(angle)
            pin0.write_analog(angle)
            sleep(time)
    if button_b.was_pressed():
        if angle > 20:
            angle = angle - 10
            print(angle)
            pin0.write_analog(angle)
            sleep(time)
