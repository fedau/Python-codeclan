from db.run_sql import run_sql

from models.task import Task
  
def select_all():  
    tasks = [] 

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        task = Task(row['description'], row['assignee'], row['duration'], row['completed'], row['id'] )
        tasks.append(task)
    return tasks 

def save(task):
    sql = f"""INSERT INTO tasks (description, assignee, duration, completed) 
    VALUES (%s, %s, %s, %s) RETURNING * """
    values = [ task.description, task.assignee,task.duration,task.completed ]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    return task


def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values= [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        task = Task(result['description'],result['assignee'] , result['duration'], result['completed'],result['id'])
        return task
    
def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)
