from microbit import *

pin0.write_analog(0)

min = 20
max = 100
jump = 5
time = 500

while True:
    for i in range(min/jump, max/jump):
        pin0.write_analog(i * jump)
        # print(i * jump)
        sleep(time)
    for i in range(min/jump, max/jump):
        pin0.write_analog(max - (i * jump) + min)
        # print(max - (i * jump) + min)
        sleep(time)
