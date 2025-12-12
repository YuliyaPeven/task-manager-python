from database import create_table
from services import (
    add_task,
    get_tasks,
    get_tasks_by_status,
    delete_task,
    update_task_status,
    export_to_csv
)

def menu():
    print("\n--- TASK MANAGER ---")
    print("1. Add task")
    print("2. Show all tasks")
    print("3. Update task status")
    print("4. Delete task")
    print("5. Show tasks by status")
    print("6. Export to CSV")
    print("0. Exit")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for t in tasks:
        print(f"{t[0]}. {t[1]}  [{t[2]}]  Deadline: {t[3]}")

def main():
    create_table()

    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            deadline = input("Deadline (YYYY-MM-DD) or leave empty: ")
            if deadline.strip() == "":
                deadline = None
            add_task(title, deadline)
            print("Task added.")

        elif choice == "2":
            tasks = get_tasks()
            show_tasks(tasks)

        elif choice == "3":
            task_id = input("Task ID: ")
            status = input("New status (todo/in progress/done): ")
            update_task_status(task_id, status)
            print("Status updated.")

        elif choice == "4":
            task_id = input("Task ID: ")
            delete_task(task_id)
            print("Task deleted.")

        elif choice == "5":
            status = input("Status (todo/in progress/done): ")
            tasks = get_tasks_by_status(status)
            show_tasks(tasks)

        elif choice == "6":
            export_to_csv()
            print("Exported to tasks_export.csv")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
