import sqlite3
import config

class db:

    def connect(self):
        gv = config.global_var()
        # Connect to the database. If the database doesn't exist, it will be created.
        con = sqlite3.connect(gv.database)
        cur = con.cursor()
        return con,cur

    def start(self):
        con,cur = self.connect()
        sql = "CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY,taskname TEXT,description TEXT,serverIP TEXT,sensors TEXT,plugins TEXT,creator_id INTEGER,task_status INTEGER,accept_time TEXT)"
        cur.execute(sql)

        con.commit()
        con.close()

    def insert_task_info(self,id,taskname,description,serverIP,sensors,plugins,creator_id,task_status,take_time,upload_frequency):
        con, cur = self.connect()
        cur.execute('insert into tasks values (?,?,?,?,?,?,?,?,?,?)',(id,taskname,description,serverIP,sensors,plugins,creator_id,task_status,take_time,upload_frequency))

        con.commit()
        con.close()

    # Insert sensed data into the database.
    def insert_data(self,id,time_stamp,gps,motion,temperature,humidity,co2,air_pressure,helmet_motion):
        con, cur = self.connect()
        cur.execute('insert into Sensed_data values (?,?,?,?,?,?,?,?)',(id,time_stamp,gps,motion,temperature,humidity,co2,air_pressure,helmet_motion))

        con.commit()
        con.close()
    
    def insert_task_sensor(self,task_id,sensor_id,sensor_frequency):
        con, cur = self.connect()
        cur.execute('insert into task_sensor(task_id,sensor_id,frequency) values (?,?,?)',(task_id,sensor_id,sensor_frequency))

        con.commit()
        con.close()

    def get_alltasks_info(self):
        con, cur = self.connect()
        alltasks_info = cur.execute('SELECT id,taskname,task_status from tasks')
        list = []
        for row in alltasks_info:
            list.append({"task_id": row[0],"task_name": row[1], "task_status": row[2]})
        con.commit()
        con.close()

        return list

    def get_task_info(self,task_id):
        con, cur = self.connect()
        cur.execute('SELECT * from tasks where id ='+task_id)
        task_info = cur.fetchall()[0]
        
        con.commit()
        con.close()
        return task_info
    
    def get_taskname_by_id(self,task_id):
        con,cur = self.connect()
        cur.execute("select taskname from tasks where id=:task_id",{"task_id":task_id})
        taskname = cur.fetchone()[0]
        con.close()
        return taskname

    def update_task_status(self,task_id,task_status):
        con,cur = self.connect()
        cur.execute("update tasks set task_status =:task_status where id=:task_id",{"task_status":task_status,"task_id":task_id})
        
        con.commit()
        con.close()

    def get_sensor_list(self,task_id):
        con,cur = self.connect()
        cur.execute("select Name from Sensors where exists (select sensor_id from task_sensor where task_sensor.sensor_id=Sensors.id AND task_sensor.task_id=:id)",{"id":task_id})
        sensor_list = cur.fetchall()

        return sensor_list

    def update_sensor_status(self,task_id,sensor_status):
        con,cur = self.connect()
        cur.execute("update task_sensor set Status =:sensor_status where task_id=:task_id",{"sensor_status":sensor_status,"task_id":task_id})
        
        con.commit()
        con.close()

    def get_task_status(self,task_id):
        con,cur = self.connect()
        cur.execute("select task_status from tasks where id=:task_id",{"task_id":task_id})
        task_status = cur.fetchone()[0]
        con.close()
        return task_status

    def delete_task(self,task_id):
        con,cur = self.connect()
        cur.execute("delete from tasks where id=:task_id",{"task_id":task_id})

        con.commit()
        con.close()
    
    def delete_task_sensor(self,task_id):
        con,cur = self.connect()
        cur.execute("delete from task_sensor where task_id=:task_id",{"task_id":task_id})

        con.commit()
        con.close()

if __name__ == '__main__':
    db = db()
    #db.insert_task(2,'test-task2','task_descr2','789.123','0,0','1,1',1,0,'then')
    #db.get_task_info()