from microbit import *

# to play this game, press the A button as many times as you can
# at the end of the time it will show your score

display.show(str("3"))
sleep(1000)
display.show(str("2"))
sleep(1000)
display.show(str("1"))
sleep(1000)
display.scroll(str("GO"))

# wait for a while
sleep(5000)
# display the number of button presses
display.scroll(str(button_a.get_presses()))
