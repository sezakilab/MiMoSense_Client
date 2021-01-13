import configparser

class global_var:

    def __init__(self):
        cf = configparser.ConfigParser()
        cf.read("config.ini")

        #secs = cf.sections()
        #print(secs)
        self.database = cf.get("Sqlite-Database", "db")
        self.device_id = cf.get("Device", "id")
        self.device_kind = cf.get("Device", "kind")
        self.device_ip = cf.get("Device", "ip")

    def get_database(self):
        return self.database

#当没有检测到config文件时，需要创建一个
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