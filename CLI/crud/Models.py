

from Database import get_connection

# C — CREATE

def add_student(name: str, age: int, course: str, marks: float) -> int:
    """
    Naya student INSERT karo.
    MySQL mein %s placeholder use hota hai (SQLite mein ? tha).
    Returns: naya student ID
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)",
        (name, age, course, marks)
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return new_id


# R — READ

def get_all_students() -> list:
    """Saare students lao — list of tuples."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY id")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_student_by_id(student_id: int):
    """ID se ek student lao. Nahi mila toh None."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row


def search_by_name(keyword: str) -> list:
    """Name mein keyword dhundo."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE name LIKE %s",
        (f"%{keyword}%",)
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_by_course(course: str) -> list:
    """Course ke hisaab se students lao."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE course LIKE %s",
        (f"%{course}%",)
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


# U — UPDATE

def update_student(student_id: int, name=None, age=None,
                   course=None, marks=None) -> bool:
    """
    Partial update — sirf jo field do, wahi badlega.
    MySQL mein bhi %s placeholder use hota hai.
    """
    old = get_student_by_id(student_id)
    if old is None:
        return False

    # old tuple: (id, name, age, course, marks)
    new_name   = name   if name   is not None else old[1]
    new_age    = age    if age    is not None else old[2]
    new_course = course if course is not None else old[3]
    new_marks  = marks  if marks  is not None else old[4]

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET name=%s, age=%s, course=%s, marks=%s WHERE id=%s",
        (new_name, new_age, new_course, new_marks, student_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return True


# D — DELETE

def delete_student(student_id: int) -> bool:
    """Student delete karo by ID."""
    if get_student_by_id(student_id) is None:
        return False

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return True


def delete_all_students() -> int:
    """Saare students delete karo. Returns: count."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]
    cursor.execute("DELETE FROM students")
    conn.commit()
    cursor.close()
    conn.close()
    return count


# EXTRA — Statistics

def get_statistics() -> dict:
    """AVG, MAX, MIN, COUNT — MySQL aggregate functions."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*), ROUND(AVG(marks),2), MAX(marks), MIN(marks) FROM students"
    )
    count, avg, hi, lo = cursor.fetchone()

    topper = None
    if count and count > 0:
        cursor.execute(
            "SELECT name, marks FROM students ORDER BY marks DESC LIMIT 1"
        )
        topper = cursor.fetchone()

    cursor.close()
    conn.close()
    return {
        "total":   count,
        "average": avg,
        "highest": hi,
        "lowest":  lo,
        "topper":  {"name": topper[0], "marks": topper[1]} if topper else None,
    }