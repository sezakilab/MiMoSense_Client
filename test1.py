import sqlite3
con = sqlite3.connect('sensing-project.db')
cur = con.cursor()
#cur.execute("create table people (name_last, age)")

who = "Yeltsin"
age = 25

id=2
task_name="Task50"
serverIP=""
task_des=""
task_sensors=None
task_plugins=""
creator_id=0

# This is the qmark style:
#cur.execute("insert into tasks(id,taskname,description) values (?,?,?)", (id, task_name,task_des))

# And this is the named style:
#cur.execute("select * from people where age=:age", {"age": age})

cur.execute("update tasks set task_status = 1 where id=:task_id",{"task_id":id})
cur.execute("update task_sensor set Status = 1 where task_id=:task_id",{"task_id":id})
con.commit()
cur.execute("update Sensors set State = 1 where exists (select sensor_id from task_sensor where task_sensor.sensor_id=Sensors.id AND Status=1);")
#print(cur.fetchone())
con.commit()
con.close()