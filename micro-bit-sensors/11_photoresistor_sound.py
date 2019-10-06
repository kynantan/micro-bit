from microbit import *
import music

frequencyRange = 4
noteLength = 6

while True:

    photoresistor = pin2.read_analog()
    music.pitch(photoresistor * frequencyRange, noteLength)
