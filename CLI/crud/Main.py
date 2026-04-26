

from Database import create_database, create_table
from Database import create_database, create_table
from Models import (
    add_student,
    get_all_students,
    get_student_by_id,
    search_by_name,
    get_by_course,
    update_student,
    delete_student,
    delete_all_students,
    get_statistics,
)
from Display import print_table, print_student, print_stats, confirm


def handle_add():
    print("\n  ── ADD NEW STUDENT ──────────────")
    name   = input("  Name   : ").strip()
    age    = int(input("  Age    : "))
    course = input("  Course : ").strip()
    marks  = float(input("  Marks  : "))
    sid = add_student(name, age, course, marks)
    print(f"\n  ✅ Student added! New ID = {sid}\n")


def handle_view_all():
    print("\n  ── ALL STUDENTS ─────────────────")
    print_table(get_all_students())


def handle_view_by_id():
    sid = int(input("\n  Enter Student ID: "))
    print_student(get_student_by_id(sid))


def handle_search_name():
    kw = input("\n  Search name (keyword): ").strip()
    print_table(search_by_name(kw))


def handle_search_course():
    kw = input("\n  Search course (keyword): ").strip()
    print_table(get_by_course(kw))


def handle_update():
    print("\n  ── UPDATE STUDENT ───────────────")
    sid = int(input("  Student ID: "))
    old = get_student_by_id(sid)
    if not old:
        print(f"\n  ❌ ID {sid} nahi mila!\n")
        return
    print_student(old)
    print("  (Enter dabao = purana value rakhna)\n")
    name_in   = input(f"  New Name   [{old[1]}]: ").strip()
    age_in    = input(f"  New Age    [{old[2]}]: ").strip()
    course_in = input(f"  New Course [{old[3]}]: ").strip()
    marks_in  = input(f"  New Marks  [{old[4]}]: ").strip()
    update_student(
        sid,
        name   = name_in   or None,
        age    = int(age_in)     if age_in   else None,
        course = course_in or None,
        marks  = float(marks_in) if marks_in else None,
    )
    print(f"\n  ✅ Updated!\n")
    print_student(get_student_by_id(sid))


def handle_delete():
    sid = int(input("\n  Student ID to delete: "))
    row = get_student_by_id(sid)
    if not row:
        print(f"\n  ❌ ID {sid} nahi mila!\n")
        return
    print(f"\n  Delete: {row[1]} (ID={sid})?")
    if confirm("Confirm"):
        delete_student(sid)
        print("\n  ✅ Deleted!\n")
    else:
        print("\n  Cancelled.\n")


def handle_delete_all():
    if confirm("⚠️  SAARE records delete karna hai"):
        count = delete_all_students()
        print(f"\n  ✅ {count} records deleted!\n")
    else:
        print("\n  Cancelled.\n")


MENU = """


CREATE   1. Add Student                
READ     2. View All Students          
         3. View by ID                 
         4. Search by Name             
         5. Search by Course           
UPDATE   6. Update Student             
DELETE   7. Delete Student             
EXTRA    8. Statistics                 
         9. Delete ALL                 
         0. Exit    
"""

HANDLERS = {
    "1": handle_add,       "2": handle_view_all,
    "3": handle_view_by_id,"4": handle_search_name,
    "5": handle_search_course, "6": handle_update,
    "7": handle_delete,    "8": lambda: print_stats(get_statistics()),
    "9": handle_delete_all,
}


def main():
    create_database()   # school_db banao agar nahi hai
    create_table()      # students table banao
    while True:
        print(MENU)
        choice = input("\n  Choice (0-9): ").strip()
        if choice == "0":
            print("\n  👋 Bye bhai!\n")
            break
        elif choice in HANDLERS:
            HANDLERS[choice]()
        else:
            print("\n  ❌ 0-9 mein se choose karo!\n")


if __name__ == "__main__":
    main()