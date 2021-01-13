from upm import pyupm_veml6070 as veml6070
import sys,signal,atexit
import Sensor

class Uv(Sensor):

    def __init__(self):
        print('start')

    def Read(self):
        veml6070_sensor = veml6070.VEML6070(0)

        def SIGINTHandler(signum, frame):
            raise SystemExit

        def exitHandler():
            print("Exiting")
            sys.exit(0)

        atexit.register(exitHandler)
        signal.signal(signal.SIGINT, SIGINTHandler)

        return veml6070_sensor.getUVIntensity()
