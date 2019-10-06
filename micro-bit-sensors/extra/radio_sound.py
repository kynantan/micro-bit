from microbit import *
import radio
import music

radio.config(channel=7)

# turn the radio on!
radio.on()

# notes in format "NOTE/OCTAVE:DURATION"
note1 = "C4:4"
note2 = "D4:4"
note3 = "E4:4"

incoming = ''

while True:
    # different buttons send different notes
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send(note3)
    elif button_b.is_pressed():
        radio.send(note2)
    elif button_a.is_pressed():
        radio.send(note1)

    sleep(1000)
    
    # Read any incoming messages
    incoming = str(radio.receive())

    # make sure there is a message
    if incoming is not 'None':
        # display.scroll(incoming)
        music.play(incoming)
