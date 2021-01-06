import Sensor

class Sensor_Manager():

    def __init__(self):

        self.current_sensors=[]

    def num_of_sensors(self):

        return len(self.current_sensors)

    def add_sensor(self,sensor):

        self.current_sensors.append(sensor)

    def remove_sensor(self,sensor):

        self.current_sensors.remove(sensor)

    def start_all_sensors(self):

        print("Start sensors.")

    def stop_all_sensors(self):

        print("Stop sensors.")