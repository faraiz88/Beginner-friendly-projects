import json
import os

FILENAME = "lists.json"

# Create file if it doesn't exist
def save_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            json.dump([], f, indent=3)

# Load tasks from file
def load_file():
    with open(FILENAME, "r") as f:
        return json.load(f)

save_file()
tasks = load_file()

def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=3)

def show_menu():
    print("\n--- TO DO LIST ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit the program")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        to_do_list = {
            "Task": task,
            "Done": False
        }
        tasks.append(to_do_list)
        save_tasks()

    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        for i, t in enumerate(tasks, start=1):
            status = "✅" if t["Done"] else "❌"
            print(f"{i}. {t['Task']} {status}")

    elif choice == "3":
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["Done"] = True
            save_tasks()

    elif choice == "4":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            save_tasks()

    elif choice == "5":
        print("Exiting....")
        break

    else:
        print("Invalid choice, try again!")
