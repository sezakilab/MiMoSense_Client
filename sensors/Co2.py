import adafruit_sgp30
import board
import busio
import Sensor

class Co2(Sensor):

    def __init__(self):
        print('start')

    def Read(self):
        i2c_CO2 = busio.I2C(board.SCL, board.SDA, frequency=100000)
        # Create library object on our I2C port
        sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c_CO2)
        print("SGP30 serial #", [hex(i) for i in sgp30.serial])
        sgp30.iaq_init()
        sgp30.set_iaq_baseline(0x8973, 0x8AAE)
        elapsed_sec = 0
        return sgp30.eCO2, sgp30.TVOC
        '''co2.append(sgp30.eCO2)
    elapsed_sec += 1
    if (elapsed_sec>10):
        elapsed_sec=0
        print( "**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x" % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))'''