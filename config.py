import configparser
import requests
from multiprocessing import Value
from pathlib import Path

class global_var:

    def __init__(self):

        cf = configparser.ConfigParser()
        #Detect config file exist or not.
        config_file=Path("config.ini")
        try:
            my_abs_path = config_file.resolve()
        except FileNotFoundError:
            #Create new config file.
            cf.add_section('Sqlite-Database')
            cf.set('Sqlite-Database','db','sensing-project.db')
            cf.add_section('Device')
            cf.set('Device','id','')
            cf.set('Device','kind','scooter')
            with open('config.ini', 'w') as fw:
                cf.write(fw)
            
        #Read from config.ini.
        cf.read("config.ini")
        self.database = cf.get("Sqlite-Database", "db")
        self.device_id = cf.get("Device", "id")
        self.device_kind = cf.get("Device", "kind")
        self.device_ip = self.get_public_IP()

    def get_public_IP(self):
        ip = requests.get('https://api.ipify.org').text
        return ip

    def setup_global_paremeters(self):
        global temperature, humidity, co2, air_pressure, motion, audio, uv, gps
        global temp_process, humidity_process, co2_process, air_pressure_process, motion_process, audio_process, uv_process, gps_process
        global mqtt_process_list

        temperature = Value('d',0.0)
        humidity = Value('d',0.0)
        co2 = Value('d',0.0)
        air_pressure = Value('d',0.0)
        motion = Value('d',0.0)
        audio = Value('d',0.0)
        uv = Value('d',0.0)
        gps = Value('d',0.0)

        temp_process = None
        humidity_process = None
        co2_process = None
        air_pressure_process = None
        motion_process = None
        audio_process = None
        uv_process = None
        gps_process = None

        mqtt_process_list = []