import json


def load_tasks():
    with open("tasks.json", "r") as f:
        return f.read()
        
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent = 4)
    
def add_task():
    description = input("Enter task description: ")
    task = {
        "task": description,
        "done": False
    }
    return task

tasks = load_tasks()          # load existing tasks
tasks.append(tasks.json)        # add new task
save_tasks(tasks)             # save updated list
    
print("Task added and saved!")