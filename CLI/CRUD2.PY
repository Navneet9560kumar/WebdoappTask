import os

FILE = "tasks.txt"

def load_tasks():
    tasks =[]
    if not os.path.exists(FILE):
        return tasks
    with open(FILE, "r")as f:
        for line in f:
            title, done = line.strip().split(" | ")
            tasks.append({"title":title,"done":done == "True"})
        return tasks
    
def save_tasks(tasks):
    with open(FILE, "w") as f:
        for t in tasks:
            f.write(f"{t['title']} | {t['done']}\n")

def create_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title,"done": False})
    save_tasks(tasks)
    print("Task added!")

def read_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return
    for i, t in enumerate(tasks):
        status = '✅' if t["done"] else '❌'
        print(f"{i}.{t['title']} - {status}")

def update_task(tasks):
    read_tasks(tasks)
    try:
        idx = int(input("Enter index: "))
        if idx <0 or idx >= len(tasks):
            print("Invalid index")
            return
        
        new_title = input("New title (Enter to skip): ")
        if new_title:
            tasks[idx]["title"] = new_title

        mark = input("Mark done? (y/n) :")
        if mark.lower() =='y':
            tasks[idx]["done"]= True

        save_tasks(tasks)
        print("Update")
    except:
        print("Invalid input")


def delete_task(tasks):
    read_tasks(tasks)
    try:
        idx =int(input("Enter index: "))
        if idx <0 or idx >= len(tasks):
            print("Invalid index")
            return
        tasks.pop(idx)
        save_tasks(tasks)
        print("Deleted")
    except:
        print("Invalid input")

def search_task(tasks):
    keyword = input("Enter keyword: ").lower()
    found = False

    for i, t in enumerate(tasks):
       if keyword in t["title"].lower():
            status = "✅" if t["done"] else "❌"
            print(f"{i}. {t['title']} - {status}")
            found = True
    
    if not found:
        print("No matching task")
    
def main():

    tasks = load_tasks()
    while True:
        print("\n1.Create\n2.Read\n3.Update\n4.Delete\n5.Search\n6.Exit")
        choice = input("Choose: ")

        if choice =="1":
            create_task(tasks)
        elif choice == "2":
            read_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice =="4":
            delete_task(tasks)
        elif choice =="5":
            search_task(tasks)
        elif choice == "6":
            print("Bye bro")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()