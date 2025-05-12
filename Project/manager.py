def add_task(tasks,task_name):
    task = {"task": task_name, "completed": False}
    tasks.append(task)
    print(f"Task: {task_name} was successfully added!")
    return

def show_tasks(tasks):
    print("\nListing your Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        task_name = task["task"]
        print(f"{index}. [{status}] {task_name}")
    return

def update_task_name(tasks, task_index, new_task_name):
    adjusted_task_index = int(task_index) - 1
    if adjusted_task_index >= 0 and adjusted_task_index < len(tasks):
        tasks[adjusted_task_index]["task"] = new_task_name
        print(f"Task {task_index} was sucessfully updated to {new_task_name}")
    else:
        print("Error. Please choose a valid task number")
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
    elif choice == "2":
        show_tasks(tasks)
    elif choice == "3":
        show_tasks(tasks)
        task_index = input("Please type the number of the task you want to update: ")
        new_task_name = input("Please type the new Task name: ")
        update_task_name(tasks, task_index, new_task_name)
    elif choice == "6":
        break

print("Software ended")