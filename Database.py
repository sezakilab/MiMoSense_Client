import sqlite3
import config

class db:

    def connect(self):
        gv = config.global_var()
        # Connect to the database. If the database doesn't exist, it will be created.
        con = sqlite3.connect(gv.database)
        cur = con.cursor()
        return con,cur

    def start(self):
        con,cur = self.connect()
        sql = "CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY,taskname TEXT,description TEXT,serverIP TEXT,sensors TEXT,plugins TEXT,creator_id INTEGER,task_status INTEGER,accept_time TEXT)"
        cur.execute(sql)

        con.commit()
        con.close()

    def insert_task(self,id,taskname,description,serverIP,sensors,plugins,creator_id,task_status,accept_time):
        con, cur = self.connect()
        cur.execute('insert into tasks values (?,?,?,?,?,?,?,?,?)',(id,taskname,description,serverIP,sensors,plugins,creator_id,task_status,accept_time))

        con.commit()
        con.close()
    
    def get_alltasks_info(self):
        con, cur = self.connect()
        alltasks_info = cur.execute('SELECT id,taskname,task_status from tasks')
        list = []
        for row in alltasks_info:
            list.append({"task_id": row[0],"task_name": row[1], "task_status": row[2]})
        con.commit()
        con.close()

        return list

    def get_task_info(self,task_id):
        con, cur = self.connect()
        task_info = cur.execute('SELECT taskname,description,serverIP,sensors,plugins,creator_id,task_status,accept_time from tasks where id ='+task_id)

        con.commit()
        con.close()
        return task_info


if __name__ == '__main__':
    db = db()
    #db.insert_task(2,'test-task2','task_descr2','789.123','0,0','1,1',1,0,'then')
    #db.get_task_info()