import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    cgpa REAL NOT NULL
)
""")
conn.commit()


def add_student():
    try:
        roll_no = int(input("Enter Scholar ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        cgpa = float(input("Enter CGPA: "))

        cursor.execute("""
        INSERT INTO students (roll_no, name, department, cgpa)
        VALUES (?, ?, ?, ?)
        """, (roll_no, name, department, cgpa))

        conn.commit()
        print("Student added successfully.")

    except sqlite3.IntegrityError:
        print("Error: Scholar ID already exists.")
    except ValueError:
        print("Error: Enter valid numeric values for Scholar ID and CGPA.")


def display_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No student records found.")
        return

    print("\n" + "-" * 65)
    print(f"{'Roll No.':<12}{'Name':<20}{'Department':<18}{'CGPA':<8}")
    print("-" * 65)

    for student in students:
        print(f"{student[0]:<12}{student[1]:<20}"
              f"{student[2]:<18}{student[3]:<8.2f}")

    print("-" * 65)


def search_student():
    try:
        roll_no = int(input("Enter Roll Number to search: "))

        cursor.execute(
            "SELECT * FROM students WHERE roll_no = ?",
            (roll_no,)
        )
        student = cursor.fetchone()

        if student:
            print("\nStudent Details")
            print("Roll Number :", student[0])
            print("Name        :", student[1])
            print("Department  :", student[2])
            print("CGPA        :", student[3])
        else:
            print("Student not found.")

    except ValueError:
        print("Error: Enter a valid roll number.")


def update_student():
    try:
        roll_no = int(input("Enter Roll Number to update: "))

        cursor.execute(
            "SELECT * FROM students WHERE roll_no = ?",
            (roll_no,)
        )

        if cursor.fetchone() is None:
            print("Student not found.")
            return

        name = input("Enter new Name: ")
        department = input("Enter new Department: ")
        cgpa = float(input("Enter new CGPA: "))

        cursor.execute("""
        UPDATE students
        SET name = ?, department = ?, cgpa = ?
        WHERE roll_no = ?
        """, (name, department, cgpa, roll_no))

        conn.commit()
        print("Student record updated successfully.")

    except ValueError:
        print("Error: Enter valid numeric values.")


def delete_student():
    try:
        roll_no = int(input("Enter Roll Number to delete: "))

        cursor.execute(
            "DELETE FROM students WHERE roll_no = ?",
            (roll_no,)
        )
        conn.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    except ValueError:
        print("Error: Enter a valid roll number.")


def main():
    while True:
        print("\n===== Student Information Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    finally:
        conn.close()
