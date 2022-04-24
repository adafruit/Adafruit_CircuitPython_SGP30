
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-sgp30/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/sgp30/en/latest/
    :alt: Documentation Status

.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/adafruit/Adafruit_CircuitPython_SGP30/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_SGP30/actions/
    :alt: Build Status

A CircuitPython driver for the Sensirion SGP30 gas sensor with eCO2 and TVOC output. This sensor uses I2C!

Installation and Dependencies
=============================
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
--------------------

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-sgp30/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-sgp30

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-sgp30

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-sgp30

Usage Notes
=============

See `the guide <https://learn.adafruit.com/adafruit-sgp30-gas-tvoc-eco2-mox-sensor/circuitpython-wiring-test>`_
for wiring and installation instructions.

First, import the library:

.. code-block:: python

    import busio
    import adafruit_sgp30

Next, initialize the I2C bus object:

.. code-block:: python

    import board
    i2c_bus = busio.I2C(board.SCL, board.SDA, frequency=100000)

Since we have the I2C bus object, we can now use it to instantiate the SGP30 object:

.. code-block:: python

    sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c_bus)

Reading from the Sensor
------------------------

To read from the sensor:

.. code-block:: python

    eCO2, TVOC = sgp30.iaq_measure()
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (eCO2, TVOC))


Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/sgp30/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_sgp30/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
