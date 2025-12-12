from database import connect
import csv

def add_task(title, deadline=None):
    with connect() as conn:
        conn.execute(
            "INSERT INTO tasks (title, deadline) VALUES (?, ?)",
            (title, deadline)
        )

def get_tasks():
    with connect() as conn:
        return conn.execute("SELECT * FROM tasks").fetchall()

def get_tasks_by_status(status):
    with connect() as conn:
        return conn.execute(
            "SELECT * FROM tasks WHERE status=?",
            (status,)
        ).fetchall()

def delete_task(task_id):
    with connect() as conn:
        conn.execute(
            "DELETE FROM tasks WHERE id=?",
            (task_id,)
        )

def update_task_status(task_id, status):
    with connect() as conn:
        conn.execute(
            "UPDATE tasks SET status=? WHERE id=?",
            (status, task_id)
        )

def export_to_csv(filename="tasks_export.csv"):
    tasks = get_tasks()
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Status", "Deadline"])
        writer.writerows(tasks)
