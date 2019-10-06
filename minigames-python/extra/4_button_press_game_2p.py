from microbit import *

aCount = 0
bCount = 0
winner = 0

display.show(str("3"))
sleep(1000)
display.show(str("2"))
sleep(1000)
display.show(str("1"))
sleep(1000)
# display.scroll(str("GO"))
# sleep(5000)
# display.scroll(str(button_a.get_presses()))

display.clear()

while True:
    display.clear()

    aCount = aCount + button_a.get_presses()
    if aCount >= 50:
        winner = 1
        break
    # display.show(str(aCount))
    anoLEDs = int(aCount / 10)
    if anoLEDs > 4:
        anoLEDs = 4
    alastLED = aCount % 10
    for x in range(0, anoLEDs):
        display.set_pixel(0, 4 - x, 9)
    if anoLEDs < 5:
        display.set_pixel(0, 4 - anoLEDs, alastLED)

    bCount = bCount + button_b.get_presses()
    if bCount >= 50:
        winner = 2
        break
    # display.show(str(aCount))
    bnoLEDs = int(bCount / 10)
    if bnoLEDs > 4:
        bnoLEDs = 4
    blastLED = bCount % 10
    for x in range(0, bnoLEDs):
        display.set_pixel(4, 4 - x, 9)
    if bnoLEDs < 5:
        display.set_pixel(4, 4 - bnoLEDs, blastLED)

    sleep(20)

while True:
    # display.scroll(winner)
    if winner == 1:
        display.show(Image.ARROW_W)
    if winner == 2:
        display.show(Image.ARROW_E)
    sleep(200)
    display.clear()
    sleep(200)
