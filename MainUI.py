import tkinter as tk
from tkinter import ttk
import QRCode as qr
import Database
import config
import Task_Manager_UI

class MainUI:

    def __init__(self):
        # intializing the window
        main_window = tk.Tk()
        main_window.title("SenScooter")
        # configuring size of the window
        main_window.geometry('400x600')
        # Forbid resize window
        main_window.resizable(0, 0)

        # Create Tab Control
        TAB_CONTROL = ttk.Notebook(main_window)
        # Tab1
        TAB1 = ttk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(TAB1, text='Task Panel')
        # Tab2
        TAB2 = ttk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(TAB2, text='Control Panel')
        # Tab3
        TAB3 = ttk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(TAB3, text='Real-time Panel')
        # Tab4
        TAB4 = ttk.Frame(TAB_CONTROL)
        TAB_CONTROL.add(TAB4, text='ESM Panel')

        TAB_CONTROL.pack(expand=1, fill="both")

        # Tab1
        Task_info_labelframe = tk.LabelFrame(TAB1, text="Task's information")
        Task_info_labelframe.pack(fill="both", expand="yes")

        # Treeview
        columns = ("task_name", "task_status")
        self.tree = ttk.Treeview(Task_info_labelframe, show="headings", columns=columns, selectmode=tk.BROWSE)

        # Setting column text in center.
        self.tree.column("task_name", anchor="center")
        self.tree.column("task_status", anchor="center")

        # Setting column text.
        self.tree.heading("task_name", text="Task")
        self.tree.heading("task_status", text="Status")

        # lists = [{"task_name": "task1", "task_status": "running"}, {"task_name": "task2", "task_status": "stop"}]
        db = Database.db()
        list = db.get_alltasks_info()

        i = 0
        for v in list:
            self.tree.insert('', i, values=(v.get("task_name"), v.get("task_status")))
            i += 1
        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree.bind("<Double-1>",self.treeview_doubleclick)

        Task_info_scrollbar = tk.Scrollbar(self.tree)
        Task_info_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        New_task_but = tk.Button(TAB1, text='New Task', command=qr.Scancode)
        New_task_but.pack(side=tk.RIGHT)

        Dev_info_labelframe = tk.LabelFrame(TAB1, text="Device's information")
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

        '''
        #Req_sensors_labelframe
        canvas = tk.Canvas(Req_sensors_labelframe, width=50,height=65)
        gps_icon = tk.PhotoImage(file="pics\GPS2.png")
        image = canvas.create_image(0,0,anchor='nw',image=gps_icon)
        canvas.pack(side="left")

        #Checkbox for every sensor.
        gps = ttk.Checkbutton(Req_sensors_labelframe,text='GPS',takefocus=0).place(x=40,y=30)
        '''

        # Tab2

        Sensors_labelframe = tk.LabelFrame(TAB2, text="Sensors")
        Sensors_labelframe.pack(fill="both", expand="yes")

        Plugins_labelframe = tk.LabelFrame(TAB2, text="Plugins")
        Plugins_labelframe.pack(fill="both", expand="yes")

        # Calling Main()
        main_window.mainloop()

    def treeview_doubleclick(self,event):
        item= self.tree.selection()[0]
        print("you clicked on", self.tree.item(item, "text"))
        tm = Task_Manager_UI.Task_Manager_UI(1)



if __name__ == '__main__':
    mainui = MainUI()