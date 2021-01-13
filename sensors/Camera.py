from picamera import PiCamera
import Sensor


class Camera:

    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 15