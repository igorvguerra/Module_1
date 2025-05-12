def add_task(tasks,task_name):
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    print(f"Task {task_name} was successfully added!")
    return

tasks = []


while True:
    print("\n Task Manager Menu:")
    print("1. Add a new Task")
    print("2. List your Tasks")
    print("3. Update a Task")
    print("4. Complete a Task")
    print("5. Delete a Task")
    print("6. Exit")

    choice = input("Choose your action: ")
    if choice == "1":
        task_name = input("Please type the name of the task you want to add: ")
        add_task(tasks, task_name)

    elif choice == "6":
        break

print("Software ended")