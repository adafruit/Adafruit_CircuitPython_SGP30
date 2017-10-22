import board
import busio
import time
from adafruit_sgp30 import adafruit_sgp30

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
 
# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
 
print("SGP30 serial #", [hex(i) for i in sgp30._serial])

sgp30.sgp_iaq_init()
sgp30.sgp_set_iaq_baseline(0x8973, 0x8aae)

elapsed_sec = 0

while True:
    co2eq, tvoc = sgp30.sgp_iaq_measure()
    print("CO2eq = %d ppm \t TVOC = %d ppb" % (co2eq, tvoc))
    time.sleep(1)
    elapsed_sec += 1
    if elapsed_sec > 10:
        elapsed_sec = 0
        co2eq_base, tvoc_base = sgp30.sgp_get_iaq_baseline()
        print("**** Baseline values: CO2eq = 0x%x, TVOC = 0x%x" % (co2eq_base, tvoc_base))
