import configparser
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

