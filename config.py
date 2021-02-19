import configparser
import requests
from multiprocessing import Value

class global_var:

    def __init__(self):
        cf = configparser.ConfigParser()
        cf.read("config.ini")

        #secs = cf.sections()
        #print(secs)
        self.database = cf.get("Sqlite-Database", "db")
        self.device_id = cf.get("Device", "id")
        self.device_kind = cf.get("Device", "kind")
        self.device_ip = self.get_public_IP()

    def get_public_IP(self):
        ip = requests.get('https://api.ipify.org').text
        return ip

    def get_database(self):
        return self.database

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

#Need to setup a config file if didn't detect it.
'''
import requests

def get():
    # Requests data from page
    response = requests.get("https://api.ipify.org/?format=text")
    ip = response.text

    return ip

cf = configparser.ConfigParser()

cf.add_section('Sqlite-Database')
cf.set('Sqlite-Database','host','')
cf.set('Sqlite-Database','user','')
cf.set('Sqlite-Database','password','')
cf.set('Sqlite-Database','db','')
cf.set('Sqlite-Database','charset','utf8')

cf.add_section('Device')
cf.set('Device','id','')
cf.set('Device','kind','scooter')
cf.set('Device','ip',get())

with open('config.ini', 'w') as fw:
    cf.write(fw)\

'''