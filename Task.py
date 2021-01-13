import tkinter.messagebox

class Task():

    #Initlize the task information.
    def __init__(self,id,task_name,serverIP,task_des,task_sensors,task_plugins,creator_id):
        self.id=id
        self.task_name=task_name
        self.serverIP=serverIP
        self.task_des=task_des
        self.task_sensors=task_sensors
        self.task_plugins=task_plugins
        self.creator_id=creator_id
        #Task status in client device, false at the beginning.
        self.task_status=False
        #Task's task time.
        #self.take_time=

    def write_to_database(self):
        print("Wrote to database!")

    def start(self):
        print(self.task_name+" just started!")

    def stop(self):
        print(self.task_name + " just stoped!")

    def delete(self):

        #Need to pop up the messagebox and ask user to confirm delete.
        confirm_delete = tkinter.messagebox.askokcancel('Confirm Delete','Delete this task?')
        if(confirm_delete):
            #Edit the database and make the task disappear.
            #Change the task_status to '2'.

            print('Just deleted task'+self.task_name)
