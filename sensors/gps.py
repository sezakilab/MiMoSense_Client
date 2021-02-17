#Used GPS6MV2 module in this project.
import serial
import pynmea2

class gps:

    def parseGPS(str):
        if str.find('GGA') > 0:
            msg = pynmea2.parse(str)
            print "Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s" % (msg.timestamp,msg.lat,msg.lat_dir,msg.lon,msg.lon_dir,msg.altitude,msg.altitude_units)

    def print_gps_data():
        serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
        str = serialPort.readline()
        parseGPS(str)

    def read_gps_data():
        