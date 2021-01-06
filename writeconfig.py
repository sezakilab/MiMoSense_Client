import configparser

cf = configparser.ConfigParser()

cf.add_section('Sqlite-Database')
cf.set('Sqlite-Database','host','')
cf.set('Sqlite-Database','user','')
cf.set('Sqlite-Database','password','')
cf.set('Sqlite-Database','db','')
cf.set('Sqlite-Database','charset','utf8')

cf.add_section('Device')
cf.set('Device','name','')
cf.set('Device','id','')
cf.set('Device','kind','scooter')

with open('config.ini', 'w') as fw:
    cf.write(fw)