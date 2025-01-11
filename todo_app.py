todo_task = []
task_status = []

def addTask():
    task = input("Enter the task: ")
    if task.strip() == "":
        print("Enter the task")
    else:
        todo_task.append(task)
        task_status.append("incomplete")

def viewTask():
    if len(todo_task) == 0:
        print("No tasks to display")
    else:
        for i, (task, status) in enumerate(zip(todo_task, task_status), 1):
            print(f"{i} - {task}: {status}")

def updateTask():
    try:
        task_num = int(input("Enter task number: "))
        if 1 <= task_num <= len(task_status):
            task_status[task_num - 1] = "complete"
        else:
            print("Invalid task number")
    except ValueError:
        print( "Enter a valid number.")

def visualize():
    import matplotlib.pyplot as plt
    categories = ["complete", "incomplete"]
    counts = [task_status.count("complete"), task_status.count("incomplete")]
    plt.bar(categories, counts)
    plt.title("Task Bar")
    plt.xlabel("Task Status")
    plt.ylabel("Counts")
    plt.show()

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Visualize Tasks")
    print("5. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        addTask()
    elif choice == "2":
        viewTask()
    elif choice == "3":
        updateTask()
    elif choice == "4":
        visualize()
    elif choice == "5":
        break
    else:
        print("Invalid choice, please try again.")