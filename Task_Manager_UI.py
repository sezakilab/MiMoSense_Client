import tkinter as tk
from tkinter import ttk
import Database
import os
import Sensor
import Communication

class Task_Manager_UI:

    def __init__(self,task_id):

        self.task_id = task_id
        # Configuring the task window, forbid resize window.
        task_window = tk.Tk()
        task_window.title("Task Manage")
        task_window.geometry('400x200')
        task_window.resizable(0, 0)

        #Display all the information of the task.
        tk.Label(task_window, text="Task Name").grid(row=1, column=0)
        tk.Label(task_window, text="Task Status").grid(row=2, column=0)
        tk.Label(task_window, text="Task Description").grid(row=3, column=0)
        tk.Label(task_window, text="Server IP").grid(row=4, column=0)
        tk.Label(task_window, text="Sensors").grid(row=5, column=0)
        tk.Label(task_window, text="Plugins").grid(row=6, column=0)
        tk.Label(task_window, text="Accept Time").grid(row=7, column=0)

        # Get task's information from the database.
        self.db = Database.db()
        self.taskname= self.db.get_taskname_by_id(task_id)

        # Set up the buttons for task.
        Start_task_but = tk.Button(task_window,text='Start Task',command=self.start_task)
        Stop_task_but = tk.Button(task_window, text='Stop Task',command=self.stop_task)
        Delete_task_but = tk.Button(task_window, text='Delete Task',command=self.delete_task)
        Start_task_but.grid(row=1, column=2)
        Stop_task_but.grid(row=2, column=2)
        Delete_task_but.grid(row=3, column=2)

        task_window.mainloop()

    def start_task(self):
        
        con,cur = self.db.connect()
        
        self.db.update_task_status(self.task_id,1)
        self.db.update_sensor_status(self.task_id,1)
        
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
        self.db.update_task_status(self.task_id,0)
        self.db.update_sensor_status(self.task_id,0)
        
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
        
        status = self.db.get_task_status(self.task_id)
        if (status == 1):
            tk.messagebox.showwarning(title="Warning", message="Task needs to be stopped before deleted")
        else:
            self.db.delete_task(self.task_id)
            self.db.delete_task_sensor(self.task_id)
            print('Deleted task', self.task_id)
    
    def start_task_test(self):
        print("Started the task")

if __name__ == '__main__':
    print('')
    tm = Task_Manager_UI(1)