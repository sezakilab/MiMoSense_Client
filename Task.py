import tkinter.messagebox
import paho.mqtt.publish as publish
import Database

class Task():

    #Initlize the task information.
    def __init__(self,id=0,task_name="",serverIP="",task_des="",task_sensors=None,creator_id=0, created_at=""):

        self.id=id
        self.task_name=task_name
        self.serverIP=serverIP
        self.task_des=task_des
        self.task_sensors=task_sensors
        self.task_plugins=""
        self.creator_id=creator_id
        #Task status in client device, false at the beginning.
        self.task_status=False
        #Task's task time.
        self.take_time=created_at

    def write_to_database(self):

        db = Database.db()
        con,cur = db.connect()
        cur.execute("insert into tasks values (?,?,?,?,?,?,?,?)",(self.id,self.task_name,self.task_des,self.serverIP,self.task_plugins,self.creator_id,self.task_status,self.take_time))
        count = 0
        # print("HELOO",type(self.task_sensors))
        for x in self.task_sensors:
                count=count+1
                if(self.task_sensors[x]==True):
                    cur.execute("insert into task_sensor(task_id,sensor_id) values (?,?)",(self.id,count))

        con.commit()
        con.close()
        print("Wrote to database!")

    def start(self):

        print(self.task_name+" just started!")
        #Store the collected data into the database and send them by MQTT.
        #Use json format to send data.
        sensor_co2=sensors.Co2.Co2()
        data = sensor_co2.Read()
        publish.single("test", data, hostname=self.serverIP)

    def stop(self):

        print(self.task_name + " just stoped!")

    def delete(self):

        #Need to pop up the messagebox and ask user to confirm delete.
        confirm_delete = tkinter.messagebox.askokcancel('Confirm Delete','Delete this task?')

        if(confirm_delete):
            #Edit the database and make the task disappear.
            #Change the task_status to '2'.
            print('Just deleted task'+self.task_name)