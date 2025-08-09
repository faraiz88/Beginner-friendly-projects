import json
import os


FILENAME = "lists.json"
def save_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            json.dump([], f, indent = 3)

def load_file():
    with open(FILENAME, "r") as f:
        return json.load(f)

save_file()
tasks = load_file()


def show_menu():
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


    elif choice == "2":
        for t in enumerate(tasks):
            status = "✅" if t["Done"] else "❌"

    elif choice == "3":
        mark = input("Task done? (y/n): ")
        if mark == "y":
            tasks[0]["Done"] = True
        else:
            tasks[0]["Done"] = False


    elif choice == "5":
        print("Exiting....")
        break