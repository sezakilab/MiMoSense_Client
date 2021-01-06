import configparser

cf = configparser.ConfigParser()
cf.read("config.ini")

secs = cf.sections()
print(secs)


'''options = cf.options("Mysql-Database")
print(options)

items = cf.items("Mysql-Database")
print(items)'''

host = cf.get("Device", "kind")
print(host)

#当没有检测到config文件时，需要创建一个
