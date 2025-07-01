tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def todo_app():
    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
        choice = input("Choose an option: ")
        match choice:
            case '1': add_task()
            case '2': view_tasks()
            case '3': remove_task()
            case '4': break
            case _: print("Invalid choice.")

todo_app()
