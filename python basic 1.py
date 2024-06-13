# task_manager.py

def display_menu():
    print("\nTask Manager")
    print("1. Add a task")
    print("2. Complete a task")
    print("3. Remove a task")
    print("4. View all tasks")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

def complete_task(tasks):
    task_id = int(input("Enter the task number to complete: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
        print(f"Task '{tasks[task_id]['task']}' marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(tasks):
    task_id = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
        print(f"Task '{removed_task['task']}' removed.")
    else:
        print("Invalid task number.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx}. {task['task']} [{status}]")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            complete_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
