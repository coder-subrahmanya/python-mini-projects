#To-Do List Manager
tasks = []
completed_tasks = []

def add_task():
    add = input("Enter a task: ").lower()

    tasks.append(add)
    print(f"{add} added successfully ✓")
    print()

def pending_task():
    if len(tasks) == 0:
        print("You don't have any pending task.")
        print()
    else:
        print("--Pending Tasks--")
        for index, task in enumerate(tasks, start= 1):
            print(f"{index}. {task}")

def completed_task():
    if len(completed_tasks) == 0:
        print("You have not completed any task.")
        print()
    else:
        print("--Completed Tasks--")
        for index, task in enumerate(completed_tasks, start= 1):
            print(f"{index}. {task}")

def mark_done():
    mark = input("Enter the task to mark as done: ").lower()

    if mark in tasks:
        tasks.remove(mark)
        completed_tasks.append(mark + " ✓")
        print(f"{mark} marked as done!")
        print()

def delete_task():
    delete = input("Enter the task to delete: ").lower()

    if delete in tasks:
        tasks.remove(delete)
        print(f"{delete} deleted successfully!")
        print()
    else:
        print("Task doesn't exist.")
        
while True:
    print()
    print("""       ---Menu---
    1. Add a task
    2. View pending tasks
    3. View completed tasks
    4. Mark task as done
    5. Delete Task
    6. Exit""")
    print()

    try:
        operation = int(input("Enter the option(1-6): "))
    except ValueError:
        print("Please enter a number!")
        continue

    if operation == 1:
        add_task()
    elif operation == 2:
        pending_task()
    elif operation == 3:
        completed_task()
    elif operation == 4:
        mark_done()
    elif operation == 5:
        delete_task()
    elif operation == 6:
        break
