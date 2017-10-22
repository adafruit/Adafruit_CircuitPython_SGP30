import board
import busio
import time
from adafruit_sgp30 import adafruit_sgp30

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
 
# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
 
sgp30.sgp_iaq_init()

while True:
    co2eq, tvoc = sgp30.sgp_iaq_measure()
    print("CO2eq = %d ppm \t TVOC = %d ppb" % (co2eq, tvoc))
    time.sleep(5)
