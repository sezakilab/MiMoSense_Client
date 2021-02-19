from upm import pyupm_veml6070 as veml6070
import sys,signal,atexit
import time
import os


# Get I2C bus
def getdata(n):
	veml6070_sensor = veml6070.VEML6070(0)
	def SIGINTHandler(signum, frame):
		raise SystemExit

	def exitHandler():
		print("Exiting")
		sys.exit(0)

	atexit.register(exitHandler)
	signal.signal(signal.SIGINT, SIGINTHandler)
	while True:
		n.value = veml6070_sensor.getUVIntensity()
		time.sleep(1)