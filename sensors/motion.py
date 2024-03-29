#Used SparkFun 9DoF Sensor module in this project.
#Need to install WiringPi first, then used following python code.
#https://github.com/akimach/LSM9DS1_RaspberryPi_Library
#Above code also used C code, need to be careful.

from ctypes import *
import time

def getdata(n,frequency):

    path = "../lib/liblsm9ds1cwrapper.so"
    lib = cdll.LoadLibrary(path)

    lib.lsm9ds1_create.argtypes = []
    lib.lsm9ds1_create.restype = c_void_p

    lib.lsm9ds1_begin.argtypes = [c_void_p]
    lib.lsm9ds1_begin.restype = None

    lib.lsm9ds1_calibrate.argtypes = [c_void_p]
    lib.lsm9ds1_calibrate.restype = None

    lib.lsm9ds1_gyroAvailable.argtypes = [c_void_p]
    lib.lsm9ds1_gyroAvailable.restype = c_int
    lib.lsm9ds1_accelAvailable.argtypes = [c_void_p]
    lib.lsm9ds1_accelAvailable.restype = c_int
    lib.lsm9ds1_magAvailable.argtypes = [c_void_p]
    lib.lsm9ds1_magAvailable.restype = c_int

    lib.lsm9ds1_readGyro.argtypes = [c_void_p]
    lib.lsm9ds1_readGyro.restype = c_int
    lib.lsm9ds1_readAccel.argtypes = [c_void_p]
    lib.lsm9ds1_readAccel.restype = c_int
    lib.lsm9ds1_readMag.argtypes = [c_void_p]
    lib.lsm9ds1_readMag.restype = c_int

    lib.lsm9ds1_getGyroX.argtypes = [c_void_p]
    lib.lsm9ds1_getGyroX.restype = c_float
    lib.lsm9ds1_getGyroY.argtypes = [c_void_p]
    lib.lsm9ds1_getGyroY.restype = c_float
    lib.lsm9ds1_getGyroZ.argtypes = [c_void_p]
    lib.lsm9ds1_getGyroZ.restype = c_float

    lib.lsm9ds1_getAccelX.argtypes = [c_void_p]
    lib.lsm9ds1_getAccelX.restype = c_float
    lib.lsm9ds1_getAccelY.argtypes = [c_void_p]
    lib.lsm9ds1_getAccelY.restype = c_float
    lib.lsm9ds1_getAccelZ.argtypes = [c_void_p]
    lib.lsm9ds1_getAccelZ.restype = c_float

    lib.lsm9ds1_getMagX.argtypes = [c_void_p]
    lib.lsm9ds1_getMagX.restype = c_float
    lib.lsm9ds1_getMagY.argtypes = [c_void_p]
    lib.lsm9ds1_getMagY.restype = c_float
    lib.lsm9ds1_getMagZ.argtypes = [c_void_p]
    lib.lsm9ds1_getMagZ.restype = c_float

    lib.lsm9ds1_calcGyro.argtypes = [c_void_p, c_float]
    lib.lsm9ds1_calcGyro.restype = c_float
    lib.lsm9ds1_calcAccel.argtypes = [c_void_p, c_float]
    lib.lsm9ds1_calcAccel.restype = c_float
    lib.lsm9ds1_calcMag.argtypes = [c_void_p, c_float]
    lib.lsm9ds1_calcMag.restype = c_float

    imu = lib.lsm9ds1_create()
    lib.lsm9ds1_begin(imu)
    if lib.lsm9ds1_begin(imu) == 0:
        print("Failed to communicate with LSM9DS1.")
        quit()
    lib.lsm9ds1_calibrate(imu)

    while True:
        sensed_data = ""

        for i in range(1, frequency+1):

            while lib.lsm9ds1_gyroAvailable(imu) == 0:
                pass
            lib.lsm9ds1_readGyro(imu)
            while lib.lsm9ds1_accelAvailable(imu) == 0:
                pass
            lib.lsm9ds1_readAccel(imu)
            while lib.lsm9ds1_magAvailable(imu) == 0:
                pass
            lib.lsm9ds1_readMag(imu)

            gx = lib.lsm9ds1_getGyroX(imu)
            gy = lib.lsm9ds1_getGyroY(imu)
            gz = lib.lsm9ds1_getGyroZ(imu)

            ax = lib.lsm9ds1_getAccelX(imu)
            ay = lib.lsm9ds1_getAccelY(imu)
            az = lib.lsm9ds1_getAccelZ(imu)

            mx = lib.lsm9ds1_getMagX(imu)
            my = lib.lsm9ds1_getMagY(imu)
            mz = lib.lsm9ds1_getMagZ(imu)

            cgx = lib.lsm9ds1_calcGyro(imu, gx)
            cgy = lib.lsm9ds1_calcGyro(imu, gy)
            cgz = lib.lsm9ds1_calcGyro(imu, gz)

            cax = lib.lsm9ds1_calcAccel(imu, ax)
            cay = lib.lsm9ds1_calcAccel(imu, ay)
            caz = lib.lsm9ds1_calcAccel(imu, az)

            cmx = lib.lsm9ds1_calcMag(imu, mx)
            cmy = lib.lsm9ds1_calcMag(imu, my)
            cmz = lib.lsm9ds1_calcMag(imu, mz)

            print("Gyro: %f, %f, %f [deg/s]" % (cgx, cgy, cgz))
            print("Accel: %f, %f, %f [Gs]" % (cax, cay, caz))
            print("Mag: %f, %f, %f [gauss]" % (cmx, cmy, cmz))
            sensed_data =sensed_data+";"+str(cgx)+","+str(cgy)+","+str(cgz)+","+str(cax)+","+str(cay)+","+str(caz)+","+str(cmx)+","+str(cmy)+","+str(cmz)
        n.value =sensed_data
        time.sleep(1.0)