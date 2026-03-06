import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    task = input("Enter new task: ")
    tasks = load_tasks()
    tasks.append({"task": task})
    save_tasks(tasks)
    print("✅ Task added successfully!")


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']}")

def prioritize_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to prioritize.")
        return

    sorted_tasks = sorted(tasks, key=lambda x: len(x["task"]), reverse=True)

    print("\nPrioritized Tasks:")
    for i, task in enumerate(sorted_tasks, start=1):
        print(f"{i}. {task['task']}")

def generate_schedule():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return

    print("\nDaily Schedule")
    print("--------------")

    total = len(tasks)
    morning = tasks[: total // 3]
    afternoon = tasks[total // 3 : 2 * total // 3]
    evening = tasks[2 * total // 3 :]

    print("\nMorning:")
    for t in morning:
        print("-", t["task"])

    print("\nAfternoon:")
    for t in afternoon:
        print("-", t["task"])

    print("\nEvening:")
    for t in evening:
        print("-", t["task"])

def main():

    while True:
        print("\n====== Personal Task Manager Agent ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Prioritize Tasks")
        print("4. Generate Daily Schedule")
        print("5. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            prioritize_tasks()

        elif choice == "4":
            generate_schedule()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()