from upm import pyupm_veml6070 as veml6070
import sys,signal,atexit
import time
import os

# Get I2C bus
# Get frequency's (number in one second) data reading, then store it into n value.
def getdata(n,frequency):
	veml6070_sensor = veml6070.VEML6070(0)
	def SIGINTHandler(signum, frame):
		raise SystemExit

	def exitHandler():
		print("Exiting")
		sys.exit(0)

	atexit.register(exitHandler)
	signal.signal(signal.SIGINT, SIGINTHandler)
	while True:
		sensed_data=""
		for i in range(1,frequency+1):
			sensed_data=sensed_data+";"+veml6070_sensor.getUVIntensity()
		n.value = sensed_data
		time.sleep(1)