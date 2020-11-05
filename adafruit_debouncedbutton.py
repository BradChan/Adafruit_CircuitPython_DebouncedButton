# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2020 hiibot for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_debouncedbutton`
================================================================================

CircuitPython button debouncer


* Author(s): hiibot

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s). Use unordered list & hyperlink rST
   inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_DebouncedButton.git"

import time


class Debouncer:
    """Debounce an input button"""

    def __init__(self, btnpin, dbt=0.01, invert=False):
        """Make am instance.
        :param DigitalInOut: the DigitalIO to debounce
        :param int interval: bounce threshold in seconds (default is 0.010, i.e. 10 milliseconds)
        :param bool: invert
        """
        self._pin = btnpin
        self._dbtime = dbt
        self._invert = invert
        self._state = self._pin.value
        if self._invert:
            self._state = not self._state
        self._laststate = self._state
        self._time = time.monotonic()
        self._lasttime = self._time
        self._lastchgtime = self._time
        self._presstime = self._time
        self._changed = False
        self._rok = False

    def read(self):
        nowt = time.monotonic()
        nowv = self._pin.value
        if self._invert:
            nowv = not nowv
        if (nowt - self._lastchgtime) < self._dbtime:
            self._lasttime = self._time
            self._time = nowt
            self._changed = False
            return self._state
        else:
            self._lasttime = self._time
            self._time = nowt
            self._laststate = self._state
            self._state = nowv
            if self._state != self._laststate:
                self._lastchgtime = nowt
                self._changed = True
                self._rok = False
                # self._longPressed = False
                if self._state:
                    self._presstime = self._time
            else:
                self._changed = False
            return self._state

    @property
    def isPressed(self):
        """Return the current isPressed value."""
        return self._state

    @property
    def isReleased(self):
        """Return the current isReleased value."""
        return not self._state

    @property
    def wasPressed(self):
        """Return the current wasPressed value."""
        return self._state and self._changed

    @property
    def wasReleased(self):
        """Return the current wasReleased value."""
        return not self._state and self._changed

    def pressedFor(self, lent):
        """Return pressed value."""
        if self._rok:
            return False
        else:
            if (self._time - self._lastchgtime) >= lent:
                self._rok = True
        return self._state and self._rok
