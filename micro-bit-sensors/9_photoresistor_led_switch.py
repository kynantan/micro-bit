from microbit import *

calibrationVal = pin2.read_analog()

while True:
    photoresistor = pin2.read_analog()
    if photoresistor < calibrationVal - 50:
        pin16.write_digital(1)
    else:
        pin16.write_digital(0)
