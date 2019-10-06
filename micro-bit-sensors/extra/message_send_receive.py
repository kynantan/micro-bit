from microbit import *
import radio

radio.config(channel=7)
# turn the radio on!
radio.on()

message = 'hello!'
incoming = ''

while True:
    # Button A sends a "flash" message.
    if button_a.was_pressed():
        radio.send(message)  # a-ha

    # Read any incoming messages.
    incoming = str(radio.receive())

    if incoming is not 'None':
        display.scroll(incoming)
