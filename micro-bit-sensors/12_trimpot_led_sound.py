from microbit import *
import music

frequencyRange = 4
noteLength = 6

while True:
    potVal = pin2.read_analog()
    pin16.write_analog(potVal * 0.25)

    music.pitch(potVal * frequencyRange, noteLength)
