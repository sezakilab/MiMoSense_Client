import Database
import os
import Sensor
import config
import paho.mqtt.publish as publish
from multiprocessing import Process, Value, Array
import json
import time

def start_sending(id):

    db = Database.db()
    task_name = db.get_taskname_by_id(id)
 
    p = Process(name=task_name,target=send_to_server, args=(id, config.temperature, config.humidity,
                config.gps,config.co2,config.air_pressure,
                config.motion,config.audio,config.uv,))
    p.daemon = True
    p.start()
    config.mqtt_process_list.append(p)
'''
	cur.execute("select Name from Sensors where exists (select sensor_id from task_sensor where task_sensor.sensor_id=Sensors.id AND task_senser.task_id=:id)",{"id":id})
    sending_sensor_list = cur.fetchall()
    for row in sending_sensor_list:
		sensor_name = row[0]
		if sensor_name == "temperature":
			arg_tuple.append(settings.temperature)
		else if sensor_name == "humidity":
			arg_tuple.append(settings.humidity)
'''	

def stop_sending(taskname):
	print(taskname)
	for p in config.mqtt_process_list:
		print(p.name)
		if (p.name == taskname):
			p.terminate()
			config.mqtt_process_list.remove(p)

# Sending sensed data to server side in setting's frequency.
def send_to_server(task_id, temp, humid, gps, co2, air, motion, audio, uv):

    db = Database.db()
    con,cur = db.connect()
    cur.execute("select Name from Sensors where exists (select sensor_id from task_sensor where task_sensor.sensor_id=Sensors.id AND task_sensor.task_id=:id)",{"id":task_id})
    sending_sensor_list = cur.fetchall()
    # print(sending_sensor_list)
    cur.execute("select * from tasks where id=:id",{"id":task_id})
    task_info=cur.fetchall()[0]
    # print(task_info)
    con.close()
    data = {
        "task_name": task_info[1],
        "task_id":task_info[0], 
        "creator_id":task_info[5],
        "temperature": None,
        "humidity": None,
	    "co2": None,
	    "air_pressure": None,
	    "motion" : None,
	    "audio" : None,
	    "uv" : None,
	    "gps" : None
    }
    
    topic = str(task_info[0])+"_"+task_info[1]
    server_ip = task_info[3]
    # server_ip = "5.196.95.208"
    while True:
        for row in sending_sensor_list:
            print(row)
            sensor_name = row[0]
            if sensor_name == "temperature":
                data.update({"temperature":temp.value})
            elif sensor_name == "humidity":
                data.update({"humidity":humid.value})
            elif sensor_name == "gps":
                data.update({"gps":gps.value})
            elif sensor_name == "co2":
                data.update({"co2":co2.value})
            elif sensor_name == "air_pressure":
                data.update({"air_pressure":air.value})
            elif sensor_name == "motion":
                data.update({"motion":motion.value})
            elif sensor_name == "audio":
                data.update({"audio":audio.value})
            elif sensor_name == "uv":
                data.update({"uv":uv.value})
            
        data_json = json.dumps(data)
        print(data_json)
        publish.single(topic, data_json, hostname=server_ip)
        # System upload stops according to upload frequency.
        # Use this value temporary, this value should be stored in the database, task's table. 
        frequency = 1
        time.sleep(frequency)