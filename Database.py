import sqlite3

#Connect to the database. If the database doesn't exist, it will be created.
con = sqlite3.connect("sensing-project.db")

cur = con.cursor()

sql="CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY,taskname TEXT,description TEXT,serverIP TEXT)"
cur.execute(sql)

con.commit()
con.close()