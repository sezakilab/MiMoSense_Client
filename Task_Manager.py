import Task
import socketio
import cv2
import json

class Task_Manager():

    def __init__(self):
        self.current_tasks=[]

    # Read QRcode to connect a new task.
    def New_task(self):
        taskdata=self.Detect_and_scan()
        if(self.Confirm_data_form(taskdata)):
            print('dialog to confirm the new task')
            #Add the new task into the list.
        else:
            print('dialog to deny the task')
        #If the data form is correct, the program lead to the tkinter dialog to confirm the task.
        #Otherwise it will deny the task.
        # New the task with the data we acquire from the QR code.


    def Detect_and_scan(self):
        # set up camera object
        cap = cv2.VideoCapture(0)

        # QR code detection object
        detector = cv2.QRCodeDetector()
        while True:
            # get the image
            _, img = cap.read()
            #    print(img)
            # get bounding box coords and data
            data, bbox, _ = detector.detectAndDecode(img)
            #    print(data)

            # if there is a bounding box, draw one, along with the data
            if (bbox is not None):
                for i in range(len(bbox)):
                    cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i + 1) % len(bbox)][0]), color=(255,
                                                                                                 0, 255), thickness=2)
                cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0, 255, 0), 2)
                print(img.shape)
                if data:
                    print("data found: ", data)
                    f = open("config.txt", "wt")
                    f.write(data)
                    f.close()
                    break;
            # display the image preview
            cv2.imshow("code detector", img)
            if (cv2.waitKey(1) == ord("q")):
                break
        # free camera object and exit
        cap.release()
        cv2.destroyAllWindows()
        return data

    #Using this function to confirm the form is right or wrong for our task.
    #Only if the data contains taskname and sensors & plugins at least get one.
    def Confirm_data_form(self,data):
        form_validaity=False
        if('taskname' in data):
            form_validaity=True
        return form_validaity

