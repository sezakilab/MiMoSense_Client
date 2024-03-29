#M5 stack SGP30 module used in this project.
import time
import board
import busio
import adafruit_sgp30

# Get I2C bus
def getdata(n,frequency):
	i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
	# Create library object on our I2C port
	sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
	# print("SGP30 serial #", [hex(i) for i in sgp30.serial])
	sgp30.iaq_init()
	sgp30.set_iaq_baseline(0x8973, 0x8AAE)
	elapsed_sec = 0

	while True:
		sensed_data=""
		for i in range(1,frequency+1):
			sensed_data=sensed_data+";"+sgp30.eCO2
		# print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
		n.value = sensed_data
		time.sleep(1)