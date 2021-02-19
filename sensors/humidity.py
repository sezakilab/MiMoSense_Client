import time
import os
import random
import threading
import smbus

# Get I2C bus
def getdata(n):
	while True:
		bus = smbus.SMBus(1)

# SHT30 address, 0x44(68)
# Send measurement command, 0x2C(44)
#       0x06(06)    High repeatability measurement
		bus.write_i2c_block_data(0x44, 0x2C, [0x06])

		time.sleep(0.5)

# SHT30 address, 0x44(68)
# Read data back from 0x00(00), 6 bytes
# cTemp MSB, cTemp LSB, cTemp CRC, Humididty MSB, Humidity LSB, Humidity CRC

		data = bus.read_i2c_block_data(0x44, 0x00, 6)

# Convert the data
#	cTemp = ((((data[0] * 256.0) + data[1]) * 175) / 65535.0) - 45
#	fTemp = cTemp * 1.8 + 32	
		humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

# Output data to screen
		n.value = humidity 
		time.sleep(1)
#print ("Temperature in Fahrenheit : %.2f F" %fTemp)

