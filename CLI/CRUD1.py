import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def create_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)

def read_tasks(tasks):
    if not tasks:
        print("No tasks")
        return
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['title']} - {status}")

def update_task(tasks):
    read_tasks(tasks)
    idx = int(input("Enter index to update: "))
    if idx < 0 or idx >= len(tasks):
        print("Invalid index")
        return

    new_title = input("New title (leave empty to skip): ")
    if new_title:
        tasks[idx]["title"] = new_title

    mark = input("Mark done? (y/n): ")
    if mark.lower() == "y":
        tasks[idx]["done"] = True

    save_tasks(tasks)

def delete_task(tasks):
    read_tasks(tasks)
    idx = int(input("Enter index to delete: "))
    if idx < 0 or idx >= len(tasks):
        print("Invalid index")
        return

    tasks.pop(idx)
    save_tasks(tasks)



def search_task(tasks):
    keyword = input("Enter keyword to search :").lower()

    found = False
    print(f"\n--- Search Results for '{keyword}' ---")
    for i, t in enumerate(tasks):
        if keyword in t["title"].lower():
            status = "✅" if t["done"] else "❌"
            print(f"{i}.{t['title']} - {status}")
            found =  True

    if not found:
        print("No Matching tasks found")


def main():
    tasks = load_tasks()

    while True:
        print("\n1. Create\n2. Read\n3. Update\n4. Delete\n5. search_task\n6. Exit")
        choice = input("Choose: ")

        if choice == "1":
            create_task(tasks)
        elif choice == "2":
            read_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()