# Codmetric Task 3 - To-Do List Manager
from pathlib import Path

DATA_FILE = Path("tasks.txt")

def load_tasks():
    tasks = []
    if DATA_FILE.exists():
        for line in DATA_FILE.read_text(encoding="utf-8").splitlines():
            done, title = line.split("|", 1)
            tasks.append({"title": title, "done": done == "1"})
    return tasks

def save_tasks(tasks):
    lines = [("1" if t["done"] else "0") + "|" + t["title"] for t in tasks]
    DATA_FILE.write_text("\n".join(lines), encoding="utf-8")

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "⬜"
        print(f"{i}. {status} {t['title']}")

def add_task(tasks):
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("Task added.")

def delete_task(tasks):
    try:
        idx = int(input("Enter task number to delete: "))
        tasks.pop(idx - 1)
        print("Task deleted.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def complete_task(tasks):
    try:
        idx = int(input("Enter task number to mark complete: "))
        tasks[idx - 1]["done"] = True
        print("Task marked complete.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. View  2. Add  3. Delete  4. Complete  5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1": list_tasks(tasks)
        elif choice == "2": add_task(tasks)
        elif choice == "3": delete_task(tasks)
        elif choice == "4": complete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Saved. Bye!")
            break
        else:
            print("Invalid choice.")
        save_tasks(tasks)  # persist after each action

if __name__ == "__main__":
    main()
