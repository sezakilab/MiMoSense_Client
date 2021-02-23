# Used GPS6MV2 module in this project.

import serial
import pynmea2

def parseGPS(str):
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
        print "Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s" % (msg.timestamp, msg.lat, msg.lat_dir, msg.lon, msg.lon_dir, msg.altitude, msg.altitude_units)
        gps_data= msg.lat+","+msg.lon
        return gps_data

# Get data according to frequency (e.g., 10 times in one second.)
def print_gps_data(n,frequency):
    while True:
        sensed_data=""
        serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.2)
        for i in range(1,frequency+1):
            str = serialPort.readline()
            gps_data = parseGPS(str)
            sensed_data = sensed_data +";"+gps_data
        n.value = sensed_data
        time.sleep(1.0) 
