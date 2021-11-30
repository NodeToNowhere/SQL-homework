from db.run_sql import run_sql


# -----CREATE-----

def save(task):
    sql = "INSERT INTO tasks (description, user_id, duration, completed) VALUES (%s,%s,%s,%s) RETURNING *"
    values = [task.description, task.user.id, task.duration, task.completed]
    results = run_sql(sql, values)
    id = results[0]["id"]
    task.id = id
    return task
