from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
import QRCode as qr
import Database
import config
import Task_Manager_UI
import os

class UI:

    def __init__(self):
        
        # Intializing the window, configuring size of the window, forbid resize window.
        main_window = tk.Tk()
        main_window.title("SenScooter")
        main_window.geometry('600x800')
        main_window.resizable(0, 0)

        # Create Tabs.
        TAB_CONTROL = ttk.Notebook(main_window)
        TAB1 = ttk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(TAB1, text='Task Panel')
        TAB2 = ttk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(TAB2, text='Real-time Panel')

        TAB_CONTROL.pack(expand=1, fill="both")
        #-----------------------------Tab1------------------------------------
        # Task labelframe.
        Task_info_labelframe = tk.LabelFrame(TAB1, text="Task's information")
        Task_info_labelframe.pack(fill="both", expand="yes")

        # Treeview for tasks' information.
        columns = ("id", "task_name", "task_status")
        self.tree = ttk.Treeview(Task_info_labelframe, show="headings", columns=columns, selectmode=tk.BROWSE)

        # Setting column text in center.
        self.tree.column("id", anchor="center")
        self.tree.column("task_name", anchor="center")
        self.tree.column("task_status", anchor="center")

        # Setting column text.
        self.tree.heading("id", text="Id")
        self.tree.heading("task_name", text="Task")
        self.tree.heading("task_status", text="Status")

        # lists = [{"task_name": "task1", "task_status": "running"}, {"task_name": "task2", "task_status": "stop"}]
        self.db = Database.db()
        self.show_task_list()

        Task_info_scrollbar = tk.Scrollbar(self.tree)
        Task_info_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        # IoT device labelframe.
        Iot_info_labelframe = tk.LabelFrame(TAB1,text="IoT Device")
        Iot_info_labelframe.pack(fill="both",expand="yes")

        # Treeview2 for IoT information.
        columns2 = ("id","device_name","device_status")
        self.tree = ttk.Treeview(Iot_info_labelframe,show="headings",columns=columns2,selectmode=tk.BROWSE)

        self.tree.column("id", anchor="center")
        self.tree.column("device_name", anchor="center")
        self.tree.column("device_status", anchor="center")

        # Setting column text.
        self.tree.heading("id", text="Id")
        self.tree.heading("device_name", text="Device")
        self.tree.heading("device_status", text="Status")

        # New task, refresh button.
        New_task_but = tk.Button(TAB1, text='New Task', command=lambda:[qr.test_func(),self.reset(main_window)])
        New_task_but.pack(side=tk.RIGHT)
        Refresh_but = tk.Button(TAB1, text='Refresh', command=lambda:[self.show_task_list()])
        Refresh_but.pack(side=tk.RIGHT)

        New_device_but =tk.Button(TAB1,text="New Device")
        New_device_but.pack(side=tk.RIGHT)

        # Bicycle/scooter device labelframe.
        Dev_info_labelframe = tk.LabelFrame(TAB1, text="This Device's information")
        Dev_info_labelframe.pack(fill="both", expand="yes")

        # Dev_info_labelframe
        tk.Label(Dev_info_labelframe, text="Device ID").grid(row=1, column=0)
        tk.Label(Dev_info_labelframe, text="Device Kind").grid(row=2, column=0)
        tk.Label(Dev_info_labelframe, text="Device IP").grid(row=3, column=0)

        gv = config.global_var()
        tk.Label(Dev_info_labelframe, text=gv.device_id).grid(row=1, column=1)
        tk.Label(Dev_info_labelframe, text=gv.device_kind).grid(row=2, column=1)
        tk.Label(Dev_info_labelframe, text=gv.device_ip).grid(row=3, column=1)

        #---------------------------------------------------------------------

        #-----------------------------Tab2------------------------------------
        Sensors_labelframe = tk.LabelFrame(TAB2, text="Sensors")
        Sensors_labelframe.pack(fill="both", expand="yes")

        #Req_sensors_labelframe
        '''
        canvas = tk.Canvas(Sensors_labelframe, width=50,height=65)
        gps_icon = tk.PhotoImage(file="pics\GPS2.png")
        image = canvas.create_image(-10,-30,anchor='nw',image=gps_icon)
        canvas.pack(side="right")
        '''
        # Load all sensors' icon.
        self.load_sensor_image('pics/ic_action_accelerometer.png',20,20,Sensors_labelframe,1,"Accelerometer",main_window)
        self.load_sensor_image('pics/ic_action_ambient_noise.png',20,20,Sensors_labelframe,2,"Ambient Noise",main_window)
        self.load_sensor_image('pics/ic_action_barometer.png',20,20,Sensors_labelframe,3,"Barometer",main_window)
        self.load_sensor_image('pics/ic_action_battery.png',20,20,Sensors_labelframe,4,"Battery",main_window)
        self.load_sensor_image('pics/ic_action_communication.png',20,20,Sensors_labelframe,5,"Communication",main_window)
        #????????
        tk.Label(Sensors_labelframe, text="Linear Acceleromete").grid(row=6, column=0)
        self.load_sensor_image('pics/ic_action_wifi.png',20,20,Sensors_labelframe,7,"Network",main_window)
        self.load_sensor_image('pics/ic_action_processor.png',20,20,Sensors_labelframe,8,"Processor",main_window)
        #????????
        tk.Label(Sensors_labelframe, text="Rotation").grid(row=9, column=0)
        self.load_sensor_image('pics/ic_action_temperature.png',20,20,Sensors_labelframe,10,"Temperature",main_window)
        self.load_sensor_image('pics/co2.png',15,15,Sensors_labelframe,11,"co2",main_window)
        #????????
        tk.Label(Sensors_labelframe, text="UV").grid(row=12, column=0)
        TextUv = tk.StringVar()
        self.get_text(main_window,TextUv,"uv")
        tk.Label(Sensors_labelframe, textvariable=TextUv ,justify='right').grid(sticky='E',row=12, column=40)
        #---------
        self.load_sensor_image('pics/humidity.png',20,20,Sensors_labelframe,13,"Humidity",main_window)
        self.load_sensor_image('pics/ic_action_locations.png',20,20,Sensors_labelframe,14,"GPS",main_window)
        #---------------------------------------------------------------------

        # Show all the IoT devie's real time in this part.
        IoT_device_labelframe = tk.LabelFrame(TAB2,text="IoT Device")
        IoT_device_labelframe.pack(fill="both",expand="yes")

        Plugins_labelframe = tk.LabelFrame(TAB2, text="Plugins")
        Plugins_labelframe.pack(fill="both", expand="yes")

        # Calling Main()
        main_window.mainloop()

    #This function used to load sensors' image into Tab2's sensors_labelframe.
    def load_sensor_image(self,image_dir,resize_parameter1,resize_parameter2,labelframe,row_number,sensor_kind,window):
        image = Image.open(image_dir)
        image = image.resize((resize_parameter1, resize_parameter2), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(image)
        tk.Label(labelframe, image=icon).grid(sticky='W',row=row_number, column=1)
        tk.Label(labelframe, text="Location").grid(row=row_number, column=0)
        Text = tk.StringVar()
        self.get_text(window,Text,sensor_kind)
        tk.Label(labelframe, textvariable=Text ,justify='right').grid(sticky='E',row=row_number, column=40)

    def treeview_doubleclick(self,event):
        item = self.tree.identify('item',event.x,event.y)
        task_id = self.tree.item(item)['values'][0]
        tm = Task_Manager_UI.Task_Manager_UI(task_id)
    
    def get_text(self, root, val, name):
        lookup = {"gps": config.gps.value,
                  "co2": config.co2.value,
                  "air_pressure": config.air_pressure.value,
                  "motion": config.motion.value,
                  "audio": config.audio.value,
                  "uv": config.uv.value,
                  "humidity": config.humidity.value,
                  "temperature": config.temperature.value
                 }
        obj = lookup.get(name,None)    
        val.set(obj)
        root.after(1000,lambda:self.get_text(root,val,name))

    def create_temp_file(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        self.acc_file = os.path.join(THIS_FOLDER, 'temp/acc.txt')
        self.ambient_file = os.path.join(THIS_FOLDER, 'temp/ambient.txt')
        self.barometer_file = os.path.join(THIS_FOLDER, 'temp/barometer.txt')
        self.battery_file = os.path.join(THIS_FOLDER, 'temp/battery.txt')
        self.communication_file = os.path.join(THIS_FOLDER, 'temp/communication.txt')
     #   self.linear_acc_file = os.path.join(THIS_FOLDER, 'temp/acc.txt')
        self.network_file = os.path.join(THIS_FOLDER, 'temp/network.txt')
        self.processor_file = os.path.join(THIS_FOLDER, 'temp/processor.txt')
        self.temperature_file = os.path.join(THIS_FOLDER, 'temp/temperature.txt')
        self.co2_file = os.path.join(THIS_FOLDER, 'temp/co2.txt')
        self.uv_file = os.path.join(THIS_FOLDER, 'temp/uv.txt')
        self.humidity_file = os.path.join(THIS_FOLDER, 'temp/humidity.txt')
        self.location_file = os.path.join(THIS_FOLDER, 'temp/location.txt')

    def show_task_list(self):
        self.tree.delete(*self.tree.get_children())
        list = self.db.get_alltasks_info()
        i = 0
        for v in list:
            self.tree.insert('', i, values=(v.get("task_id"), v.get("task_name"), v.get("task_status")))
            i += 1
        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree.bind("<Double-1>",self.treeview_doubleclick)
    
    def reset(self,main_window):
        main_window.destroy()
        self.__init__()