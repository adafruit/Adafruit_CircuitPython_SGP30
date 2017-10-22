
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-adafruit_sgp30/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/adafruit_sgp30/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

This is a CircuitPython driver for the Sensirion SGP30 air quality sensor, it can provide CO2eq (equivalent CO2) and TVOC (Total Volatile Organic Compounds) with a simple I2C interface 

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

.. code-block:: python

    import board
    import busio
    import time
    import adafruit_sgp30

    i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

    # Create library object on our I2C port
    sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

    print("SGP30 serial #", [hex(i) for i in sgp30._serial])

    sgp30.sgp_iaq_init()
    while True:
        co2eq, tvoc = sgp30.sgp_iaq_measure()
        print("CO2eq = %d ppm \t TVOC = %d ppb" % (co2eq, tvoc))
        time.sleep(1)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_adafruit_sgp30/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

API Reference
=============

.. toctree::
   :maxdepth: 2

   api
