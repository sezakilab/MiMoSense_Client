import tkinter as tk
from tkinter import ttk

# intializing the window
window = tk.Tk()
window.title("SenScooter")
# configuring size of the window
window.geometry('400x600')
# Forbid resize window
window.resizable(width=False, height=False)

#Create Tab Control
TAB_CONTROL = ttk.Notebook(window)
#Tab1
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Task Panel')
#Tab2
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Control Panel')
#Tab3
TAB3 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB3, text='Real-time Panel')
#Tab4
TAB4 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB4, text='ESM Panel')

TAB_CONTROL.pack(expand=1, fill="both")
#Tab1
Task_info_labelframe = tk.LabelFrame(TAB1, text="Task's information")
Task_info_labelframe.pack(fill="both", expand="yes")

Task_info_scrollbar=tk.Scrollbar(Task_info_labelframe)
Task_info_scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)

Dev_info_labelframe = tk.LabelFrame(TAB1, text="Device's information")
Dev_info_labelframe.pack(fill="both", expand="yes")

#Dev_info_labelframe
tk.Label(Dev_info_labelframe,text="Device ID").grid(row=1,column=0)
tk.Label(Dev_info_labelframe,text="Device Name").grid(row=2,column=0)
tk.Label(Dev_info_labelframe,text="Device Kind").grid(row=3,column=0)

Dev_ID_Entry=tk.Entry(Dev_info_labelframe)
Dev_ID_Entry.grid(row=1,column=1)


'''
#Req_sensors_labelframe
canvas = tk.Canvas(Req_sensors_labelframe, width=50,height=65)
gps_icon = tk.PhotoImage(file="pics\GPS2.png")
image = canvas.create_image(0,0,anchor='nw',image=gps_icon)
canvas.pack(side="left")

#Checkbox for every sensor.
gps = ttk.Checkbutton(Req_sensors_labelframe,text='GPS',takefocus=0).place(x=40,y=30)
'''

#Tab2

Sensors_labelframe = tk.LabelFrame(TAB2, text="Sensors")
Sensors_labelframe.pack(fill="both", expand="yes")

Plugins_labelframe = tk.LabelFrame(TAB2, text="Plugins")
Plugins_labelframe.pack(fill="both", expand="yes")

#Calling Main()
window.mainloop()