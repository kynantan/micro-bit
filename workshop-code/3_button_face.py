from microbit import *

# this is a comment!
# lines that start with a # aren't treated as code
# instead you can use them to put in helpful notes

while True:
    # if the A button is pressed down
    # we want to show an image
    if button_a.is_pressed() is True:
        display.show(Image.HAPPY)
    # else if (elif) the B button is pressed down
    # we want to show a different image
    elif button_b.is_pressed() is True:
        display.show(Image.SAD)
    else:
        # clear the screen if nothing is pressed down
        display.clear()
