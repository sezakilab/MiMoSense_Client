import tkinter as tk
from tkinter import ttk
import QRCode as qr
import Database
import config
import Task_Manager_UI
import os
from PIL import ImageTk, Image
import settings

class MainUI:

    def __init__(self):
        
        # intializing the window
#        global main_window
        main_window = tk.Tk()
        main_window.title("SenScooter")
        # configuring size of the window
        
        main_window.geometry('600x800')
        # Forbid resize window
        main_window.resizable(0, 0)

        # Create Tab Control
        TAB_CONTROL = ttk.Notebook(main_window)
        # Tab1
        TAB1 = ttk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(TAB1, text='Task Panel')
        # Tab2
        TAB2 = ttk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(TAB2, text='Real-time Panel')

        # Tab3
        #TAB3 = ttk.Frame(TAB_CONTROL)
        #TAB_CONTROL.add(TAB3, text='ESM Panel')

        TAB_CONTROL.pack(expand=1, fill="both")

        # Tab1
        Task_info_labelframe = tk.LabelFrame(TAB1, text="Task's information")
        Task_info_labelframe.pack(fill="both", expand="yes")

        # Treeview
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
        

        # IoT device labelframe
        Iot_info_labelframe = tk.LabelFrame(TAB1,text="IoT Device")
        Iot_info_labelframe.pack(fill="both",expand="yes")

        #Treeview2
        columns2 = ("id","device_name","device_status")
        self.tree = ttk.Treeview(Iot_info_labelframe,show="headings",columns=columns2,selectmode=tk.BROWSE)

        self.tree.column("id", anchor="center")
        self.tree.column("device_name", anchor="center")
        self.tree.column("device_status", anchor="center")

        # Setting column text.
        self.tree.heading("id", text="Id")
        self.tree.heading("device_name", text="Device")
        self.tree.heading("device_status", text="Status")

        New_task_but = tk.Button(TAB1, text='New Task', command=lambda:[qr.test_func(),self.reset(main_window)])
        New_task_but.pack(side=tk.RIGHT)

        New_task_but = tk.Button(TAB1, text='Refresh', command=lambda:[self.show_task_list()])
        New_task_but.pack(side=tk.RIGHT)

        New_device_but =tk.Button(TAB1,text="New Device")
        New_device_but.pack(side=tk.RIGHT)

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

        # Dev_ID_Entry=tk.Entry(Dev_info_labelframe)
        # Dev_ID_Entry.grid(row=1,column=1)

        # Tab2
        Sensors_labelframe = tk.LabelFrame(TAB2, text="Sensors")
        Sensors_labelframe.pack(fill="both", expand="yes")

        

        #Req_sensors_labelframe
        '''
        canvas = tk.Canvas(Sensors_labelframe, width=50,height=65)
        gps_icon = tk.PhotoImage(file="pics\GPS2.png")
        image = canvas.create_image(-10,-30,anchor='nw',image=gps_icon)
        canvas.pack(side="right")
        '''
        image = Image.open('pics/ic_action_accelerometer.png')
        image = image.resize((20, 20), Image.ANTIALIAS)
        acc_icon = ImageTk.PhotoImage(image)
        tk.Label(Sensors_labelframe, image=acc_icon).grid(sticky='W',row=1, column=1)
        tk.Label(Sensors_labelframe, text="Accelerometer").grid(row=1, column=0)
        TextAcc = tk.StringVar()
        self.get_text(main_window,TextAcc,"motion")
        tk.Label(Sensors_labelframe, textvariable=TextAcc, justify='right').grid(sticky='E' ,row=1, column=40)
        
        image = Image.open('pics/ic_action_ambient_noise.png')
        image = image.resize((20, 20), Image.ANTIALIAS)
        ambient_icon = ImageTk.PhotoImage(image)
        tk.Label(Sensors_labelframe, image=ambient_icon).grid(sticky='W',row=2, column=1)
        tk.Label(Sensors_labelframe, text="Ambient Noise").grid(row=2, column=0)
        TextAmbient = tk.StringVar()
        self.get_text(main_window,TextAmbient,"audio")
        tk.Label(Sensors_labelframe, textvariable=TextAmbient ,justify='right').grid(sticky='E',row=2, column=40)

        image = Image.open('pics/ic_action_barometer.png')
        image = image.resize((20, 20), Image.ANTIALIAS)
        barometer_icon = ImageTk.PhotoImage(image)
        tk.Label(Sensors_labelframe, image=barometer_icon).grid(sticky='W',row=3, column=1)
        tk.Label(Sensors_labelframe, text="Barometer").grid(row=3, column=0)
        TextBarometer = tk.StringVar()
        self.get_text(main_window,TextBarometer,"air_pressure")
        tk.Label(Sensors_labelframe, textvariable=TextBarometer ,justify='right').grid(sticky='E',row=3, column=40)

        image = Image.open('pics/ic_action_battery.png')
        image = image.resize((20, 20), Image.ANTIALIAS)
        battery_icon = ImageTk.PhotoImage(image)
        tk.Label(Sensors_labelframe, image=battery_icon).grid(sticky='W',row=4, column=1)
        tk.Label(Sensors_labelframe, text="Battery").grid(row=4, column=0)
        TextBattery = tk.StringVar()
 #       self.get_text(main_window,TextBattery,self.battery_file)
        tk.Label(Sensors_labelframe, textvariable=TextBattery ,justify='right').grid(sticky='E',row=4, column=40)

        image = Image.open('pics/ic_action_communication.png')
        image = image.resize((20, 20), Image.ANTIALIAS)
        comm_icon = ImageTk.PhotoImage(image)
        tk.Label(Sensors_labelframe, image=comm_icon).grid(sticky='W',row=5, column=1)
        tk.Label(Sensors_labelframe, text="Communication").grid(row=5, column=0)
        TextCommunication = tk.StringVar()
#        self.get_text(main_window,TextCommunication,self.communication_file)
        tk.Label(Sensors_labelframe, textvariable=TextCommunication ,justify='right').grid(sticky='E',row=5, column=40)
        
        tk.Label(Sensors_labelframe, text="Linear Acceleromete").grid(row=6, column=0)
        
        image = Image.open('pics/ic_action_wifi.png')
        image = image.resize((20, 20), Image.ANTIALIAS)
        wifi_icon = ImageTk.PhotoImage(image)
        tk.Label(Sensors_labelframe, image=wifi_icon).grid(sticky='W',row=7, column=1)
        tk.Label(Sensors_labelframe, text="Network").grid(row=7, column=0)
        TextNetwork = tk.StringVar()
#        self.get_text(main_window,TextNetwork,self.network_file)
        tk.Label(Sensors_labelframe, textvariable=TextNetwork ,justify='right').grid(sticky='E',row=7, column=40)
        
        image = Image.open('pics/ic_action_processor.png')
        image = image.resize((20, 20), Image.ANTIALIAS)
        processor_icon = ImageTk.PhotoImage(image)
        tk.Label(Sensors_labelframe, image=processor_icon).grid(sticky='W',row=8, column=1)
        tk.Label(Sensors_labelframe, text="Processor").grid(row=8, column=0)
        TextProcessor = tk.StringVar()
#        self.get_text(main_window,TextProcessor,self.processor_file)
        tk.Label(Sensors_labelframe, textvariable=TextProcessor ,justify='right').grid(sticky='E',row=8, column=40)

        tk.Label(Sensors_labelframe, text="Rotation").grid(row=9, column=0)

        image = Image.open('pics/ic_action_temperature.png')
        image = image.resize((20, 20), Image.ANTIALIAS)
        temp_icon = ImageTk.PhotoImage(image)
        tk.Label(Sensors_labelframe, image=temp_icon).grid(sticky='W',row=10, column=1)
        tk.Label(Sensors_labelframe, text="Temperature").grid(row=10, column=0)
        TextTemperature = tk.StringVar()
        self.get_text(main_window,TextTemperature,"temperature")
        tk.Label(Sensors_labelframe, textvariable=TextTemperature ,justify='right').grid(sticky='E',row=10, column=40)

        image = Image.open('pics/co2.png')
        image = image.resize((15, 15), Image.ANTIALIAS)
        co2_icon = ImageTk.PhotoImage(image)
        tk.Label(Sensors_labelframe, image=co2_icon).grid(sticky='W',row=11, column=1)
        tk.Label(Sensors_labelframe, text="CO2").grid(row=11, column=0)
        TextCo2 = tk.StringVar()
        self.get_text(main_window,TextCo2,"co2")
        tk.Label(Sensors_labelframe, textvariable=TextCo2 ,justify='right').grid(sticky='E',row=11, column=40)

     
        tk.Label(Sensors_labelframe, text="UV").grid(row=12, column=0)
        TextUv = tk.StringVar()
        self.get_text(main_window,TextUv,"uv")
        tk.Label(Sensors_labelframe, textvariable=TextUv ,justify='right').grid(sticky='E',row=12, column=40)

        image = Image.open('pics/humidity.png')
        image = image.resize((20, 20), Image.ANTIALIAS)
        humidity_icon = ImageTk.PhotoImage(image)
        tk.Label(Sensors_labelframe, image=humidity_icon).grid(sticky='W',row=13, column=1)
        tk.Label(Sensors_labelframe, text="Humidity").grid(row=13, column=0)
        TextHumidity = tk.StringVar()
        self.get_text(main_window,TextHumidity,"humidity")
        tk.Label(Sensors_labelframe, textvariable=TextHumidity ,justify='right').grid(sticky='E',row=13, column=40)

        image = Image.open('pics/ic_action_locations.png')
        image = image.resize((20, 20), Image.ANTIALIAS)
        location_icon = ImageTk.PhotoImage(image)
        tk.Label(Sensors_labelframe, image=location_icon).grid(sticky='W',row=14, column=1)
        tk.Label(Sensors_labelframe, text="Location").grid(row=14, column=0)
        TextLocation = tk.StringVar()
        self.get_text(main_window,TextLocation,"gps")
        tk.Label(Sensors_labelframe, textvariable=TextLocation ,justify='right').grid(sticky='E',row=14, column=40)
        
        # Show all the IoT devie's real time in this part.
        IoT_device_labelframe = tk.LabelFrame(TAB2,text="IoT Device")
        IoT_device_labelframe.pack(fill="both",expand="yes")

        Plugins_labelframe = tk.LabelFrame(TAB2, text="Plugins")
        Plugins_labelframe.pack(fill="both", expand="yes")

        # Calling Main()
        main_window.mainloop()

    def treeview_doubleclick(self,event):
        item = self.tree.identify('item',event.x,event.y)
        task_id = self.tree.item(item)['values'][0]


        tm = Task_Manager_UI.Task_Manager_UI(task_id)
    

    def get_text(self, root, val, name):
        lookup = {"gps": settings.gps.value,
                  "co2": settings.co2.value,
                  "air_pressure": settings.air_pressure.value,
                  "motion": settings.motion.value,
                  "audio": settings.audio.value,
                  "uv": settings.uv.value,
                  "humidity": settings.humidity.value,
                  "temperature": settings.temperature.value
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

if __name__ == '__main__':
    settings.init()
    mainui = MainUI()
