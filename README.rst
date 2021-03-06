Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-debouncedbutton/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/debouncedbutton/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_DebouncedButton/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_DebouncedButton/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

CircuitPython button debouncer.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Usage Example
=============

.. code-block:: python

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


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_DebouncedButton/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
