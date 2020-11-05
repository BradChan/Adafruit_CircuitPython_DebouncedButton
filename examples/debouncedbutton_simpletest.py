# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import board
import digitalio
from adafruit_debouncedbutton import Debouncer

btnAPin = digitalio.DigitalInOut(board.D12)
btnAPin.switch_to_input(pull=digitalio.Pull.DOWN)
btnA = Debouncer(btnAPin,0.01,False)

while True:
    btnA.read()
    if btnA.isPressed:
        print("A isPressed")
    if btnA.isReleased:
        print("A isReleased")
    if btnA.wasPressed:
        print("A wasPressed")
    if btnA.wasReleased:
        print("A wasReleased")
    if btnA.pressedFor(1):
        print("A pressedFor 1")

    