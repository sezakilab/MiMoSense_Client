import smbus
import Sensor
import time

class Temp_humid(Sensor):

    def __init__(self):
        print('start')

    def Read(self):
        # Get I2C bus
        bus = smbus.SMBus(1)
        bus.write_i2c_block_data(0x44, 0x2C, [0x06])
        #time.sleep(0.5)
        data = bus.read_i2c_block_data(0x44, 0x00, 6)
        cTemp = ((((data[0] * 256.0) + data[1]) * 175) / 65535.0) - 45
        fTemp = cTemp * 1.8 + 32
        humid = 100 * (data[3] * 256 + data[4]) / 65535.0

        return humid,cTemp


