import tkinter as tk
from tkinter import ttk
import Database
import os
import Sensor
import settings
import Communication

class Task_Manager_UI:

    def __init__(self,task_id):
        self.task_id = task_id
        task_window = tk.Tk()
        task_window.title("Task Manage")
        # configuring size of the window
        task_window.geometry('400x200')
        # Forbid resize window
        task_window.resizable(0, 0)
        #Display all the information of the task.
        #First need to get information from the database.

        tk.Label(task_window, text="Task Name").grid(row=1, column=0)
        tk.Label(task_window, text="Task Status").grid(row=2, column=0)
        tk.Label(task_window, text="Task Description").grid(row=3, column=0)
        tk.Label(task_window, text="Server IP").grid(row=4, column=0)
        tk.Label(task_window, text="Sensors").grid(row=5, column=0)
        tk.Label(task_window, text="Plugins").grid(row=6, column=0)
        tk.Label(task_window, text="Accept Time").grid(row=7, column=0)
        
        self.db = Database.db()
        self.taskname= self.get_taskname_by_id()

        Start_task_but = tk.Button(task_window,text='Start Task',command=self.start_task)
        Stop_task_but = tk.Button(task_window, text='Stop Task',command=self.stop_task)
        Delete_task_but = tk.Button(task_window, text='Delete Task',command=self.delete_task)
        Start_task_but.grid(row=1, column=2)
        Stop_task_but.grid(row=2, column=2)
        Delete_task_but.grid(row=3, column=2)

        task_window.mainloop()

    def get_taskname_by_id(self):
        con,cur = self.db.connect()
        cur.execute("select taskname from tasks where id=:id",{"id":self.task_id})
        taskname = cur.fetchone()[0]
        con.close()
        return taskname


    def start_task(self):
        con,cur = self.db.connect()
    #    cur.execute("select * from tasks where id=:task_id", {"task_id": task_id})
        cur.execute("update tasks set task_status = 1 where id=:task_id",{"task_id":self.task_id})
        cur.execute("update task_sensor set Status = 1 where task_id=:task_id",{"task_id":self.task_id})
        con.commit()
        
        cur.execute("select Name from Sensors where exists (select sensor_id from task_sensor where task_sensor.sensor_id=Sensors.id AND Status=1 AND Sensors.State=0)")
        new_sensor_list = cur.fetchall()
        print("New list is : ", new_sensor_list)
        for row in new_sensor_list:
            sensor_name = row[0]
            sensor=Sensor.Sensor(sensor_name)
            print(sensor_name)
            sensor.start()
        cur.execute("update Sensors set State = 1 where exists (select sensor_id from task_sensor where task_sensor.sensor_id=Sensors.id AND Status=1);")
        #print(cur.fetchone())
        con.commit()

        print('started task ',self.task_id)
        
        Communication.start_sending(self.task_id)
        con.close()

    def stop_task(self):
        Communication.stop_sending(self.taskname)        
        con,cur = self.db.connect()
        cur.execute("update tasks set task_status = 0 where id=:task_id",{"task_id":self.task_id})
        cur.execute("update task_sensor set Status = 0 where task_id=:task_id",{"task_id":self.task_id})
        con.commit()
        
        cur.execute("select Name from Sensors where not exists (select sensor_id from task_sensor where task_sensor.sensor_id=Sensors.id AND Status=1) AND State=1")
        new_sensor_list = cur.fetchall()
        for row in new_sensor_list:
            sensor_name = row[0]
            sensor=Sensor.Sensor(sensor_name)
            sensor.stop()

        cur.execute("update Sensors set State = 0 where not exists (select sensor_id from task_sensor where task_sensor.sensor_id=Sensors.id AND Status=1);")
        #print(cur.fetchone())
        con.commit()
        
        print('stopped task', self.task_id)
        con.close()

    def delete_task(self):
        con,cur = self.db.connect()
        cur.execute("select task_status from tasks where id=:task_id",{"task_id":self.task_id})
        status = cur.fetchone()[0]
        if (status == 1):
            tk.messagebox.showwarning(title="Warning", message="Task needs to be stopped before deleted")
        else:
            cur.execute("delete from tasks where id=:task_id",{"task_id":self.task_id})
            cur.execute("delete from task_sensor where task_id=:task_id",{"task_id":self.task_id})
            con.commit()    
            print('deleted task', self.task_id)
        con.close()
    
    def start_task_test(self):
        print("started the task")

if __name__ == '__main__':
    print('')
    tm = Task_Manager_UI(1)
