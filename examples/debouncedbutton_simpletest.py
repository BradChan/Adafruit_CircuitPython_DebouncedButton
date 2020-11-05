# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import board
import digitalio
from adafruit_debouncedbutton import Debouncer

btn_a_Pin = digitalio.DigitalInOut(board.D12)
btn_a_Pin.switch_to_input(pull=digitalio.Pull.DOWN)
btn_a = Debouncer(btn_a_Pin, 0.01, False)

while True:
    btn_a.read()
    if btn_a.is_pressed:
        print("A isPressed")
    if btn_a.is_released:
        print("A isReleased")
    if btn_a.was_pressed:
        print("A wasPressed")
    if btn_a.was_released:
        print("A wasReleased")
    if btn_a.pressed_for(1):
        print("A pressedFor 1")
