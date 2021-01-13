import tkinter as tk
from tkinter import ttk
import Database

class Task_Manager_UI:

    def __init__(self,task_id):
        task_window = tk.Tk()
        task_window.title("Task Manage")
        # configuring size of the window
        task_window.geometry('400x200')
        # Forbid resize window
        task_window.resizable(0, 0)
        #Display all the information of the task.
        #First need to get information from the database.

        tk.Label(task_window, text="Task Name").grid(row=1, column=0)
        tk.Label(task_window, text="Task Status").grid(row=2, column=0)
        tk.Label(task_window, text="Task Description").grid(row=3, column=0)
        tk.Label(task_window, text="Server IP").grid(row=4, column=0)
        tk.Label(task_window, text="Sensors").grid(row=5, column=0)
        tk.Label(task_window, text="Plugins").grid(row=6, column=0)
        tk.Label(task_window, text="Accept Time").grid(row=7, column=0)

        db = Database.db()
        #task_info = db.get_task_info(taskid)

        Start_task_but = tk.Button(task_window,text='Start Task',command=self.start_task)
        Stop_task_but = tk.Button(task_window, text='Stop Task',command=self.stop_task)
        Delete_task_but = tk.Button(task_window, text='Delete Task',command=self.delete_task)
        Start_task_but.grid(row=1, column=2)
        Stop_task_but.grid(row=2, column=2)
        Delete_task_but.grid(row=3, column=2)

        task_window.mainloop()

    def start_task(self):
        print('start task')

    def stop_task(self):
        print('stop task')

    def delete_task(self):
        print('delete task')

if __name__ == '__main__':
    print('')
    tm = Task_Manager_UI(1)