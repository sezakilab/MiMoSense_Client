import tkinter
import tkinter.messagebox

def Task_dialog(is_task,data):
    if(is_task):
        accept_task = tkinter.messagebox.askokcancel('Confirm Task','Take the task?')
        if(accept_task):
            Confirm_task(data)
    else:
        tkinter.messagebox.showerror('Wrong QRcode', 'This is not a task QRcode.')


#If user confirmed to task the task, then need to communicate with the serverside,
#and write the task information into the database.
def Confirm_task(task):
    confirmed=False

    return confirmed

if __name__ == '__main__':
    Task_dialog(True,2)