from microbit import *

calibrationVal = pin2.read_analog()

while True:
    photoresistor = pin2.read_analog()

    if photoresistor > 0 and photoresistor < 512:
        lightValue = 1023 - (photoresistor * 2)
        pin16.write_analog(lightValue)
        sleep(50)
