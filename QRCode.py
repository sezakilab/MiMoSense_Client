import cv2
import json
import tkinter
import tkinter.messagebox
import Task
import requests

def Scancode():

    # set up camera object
    cap = cv2.VideoCapture(0)
    # QR code detection object
    detector = cv2.QRCodeDetector()

    while True:
        # get the image
        _, img = cap.read()
        #    print(img)
        # get bounding box coords and data
        url, bbox, _ = detector.detectAndDecode(img)
        #    print(data)
        # if there is a bounding box, draw one, along with the data.
        if (bbox is not None):
            for i in range(len(bbox)):
                cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i + 1) % len(bbox)][0]), color=(255,0, 255), thickness=2)
            cv2.putText(img, url, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
            print(img.shape)
            if url:
                print("url found: ", url)
                url = "http://"+url
                data = requests.get(url)
                data =data.json()
                Task_dialog(Task_Detect(data),data)
                break;
        # display the image preview
        cv2.imshow("code detector", img)
        if (cv2.waitKey(1) == ord("q")):
            break

    # free camera object and exit
    cap.release()
    cv2.destroyAllWindows()

'''Function for Task Detection: only with json format, and contains taskname, ip etc,

can be recognize as a task. '''

def Task_Detect(data):

    is_task = False
    if('task_id' in data) and ('task_name' in data) and ('server_ip' in data):
        is_task = True
    return is_task

#If the QRcode is the real task QRcode, then pop up to ask take it or not.
#Otherwise, pop up a dialog tells it is not a task qrcode.
def Task_dialog(is_task,data):

    if(is_task):
        accept_task = tkinter.messagebox.askokcancel('Confirm Task','Take the task?')
        if(accept_task):
            Confirm_task(data)
    else:

        tkinter.messagebox.showerror('Wrong QRcode', 'This is not a task QRcode.')

#If user confirmed to task the task, then need to communicate with the serverside,
#and write the task information into the database.
def Confirm_task(data):

    confirmed=False
    task_json = data
    task_id = task_json['task_id']
    task_name = task_json['task_name']
    task_description = task_json['task_description']
    task_sensors = task_json['task_sensors']
    # print(type(task_sensors))
    # task_plugins = task_json['task_plugins']
    task_created_at = task_json['task_created_at']
    task_creator_id = task_json['task_creator_id']
    task_certificate = task_json['task_certificate']
    server_ip = task_json['server_ip']
    #Send message to server side: device's ip, kind and so on.

    #Instance a task with the data, and add it into the task_list, write it into the database.

    newTask = Task.Task(task_id,task_name,server_ip,task_description,task_sensors, task_creator_id, task_created_at)
    newTask.write_to_database()

    #Then, reflesh the listbox.

    return confirmed

def test_func():
    data = {
        "server_ip":"5.196.95.208",
        "task_certificate":732947,
        "task_created_at":"Wed, 27 Jan 2021 02:04:25 GMT",
        "task_creator_id":2,
        "task_description":"TempHumidUVAir",
        "task_id":2,"task_name":"test_task",
        "task_sensors":{'gps': False, 'co2': True, 'air_pressure': True, 'motion': False, 'audio': False, 'uv': True, 'humidity': True, 'temp': True}
    }
    Task_dialog(Task_Detect(data),data)
    print("test here")
