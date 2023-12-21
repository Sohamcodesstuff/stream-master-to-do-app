import sqlite3


conn = sqlite3.connect("data.db",check_same_thread=False)
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS tasks(task TEXT, task_status TEXT, task_due_date DATE)")

def add_data(task, task_status, task_due_date):
    c.execute("INSERT INTO tasks(task, task_status, task_due_date) VALUES(?,?,?)",(task, task_status, task_due_date))
    conn.commit()

def view_all_data():
    c.execute("SELECT * FROM tasks")
    data = c.fetchall()
    return data

def view_unique_data():
    c.execute("SELECT task FROM tasks")
    data = c.fetchall()
    return data

def get_task(task):
    c.execute(f"SELECT * FROM tasks WHERE task='{task}'")
    data = c.fetchall()
    return data

def edit_task(task,task_status,task_due_date,new_task,new_task_status,new_task_due_date):
    c.execute("UPDATE tasks SET task=?,task_status=?,task_due_date=? WHERE task=? AND task_status=? AND task_due_date =?",(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date))
    conn.commit()
    data = c.fetchall()
    return data

def delete_task(task, task_status, task_due_date):
    c.execute("DELETE FROM tasks WHERE task=? AND task_status=? AND task_due_date=?",(task, task_status, task_due_date))
    conn.commit()

# print(view_all_data())

# c.execute("drop table tasks")
# conn.commit()

