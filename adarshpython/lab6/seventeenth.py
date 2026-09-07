import sqlite3

# Connect to database
conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    designation TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")

conn.commit()


# CREATE
def add_employee():
    print("\n--- Add Employee ---")

    try:
        emp_id = int(input("Employee ID: "))
        name = input("Name: ")
        designation = input("Designation: ")
        department = input("Department: ")
        salary = float(input("Salary: "))

        cursor.execute(
            """
            INSERT INTO employees
            (employee_id, name, designation, department, salary)
            VALUES (?, ?, ?, ?, ?)
            """,
            (emp_id, name, designation, department, salary)
        )

        conn.commit()
        print("Employee added successfully.")

    except ValueError:
        print("Please enter a valid number for Employee ID and Salary.")

    except sqlite3.IntegrityError:
        print("Employee ID already exists.")


# READ
def view_employees():
    print("\n--- Employee Records ---")

    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()

    if len(records) == 0:
        print("No employee records found.")
        return

    for employee in records:
        print("--------------------------------")
        print("Employee ID :", employee[0])
        print("Name        :", employee[1])
        print("Designation :", employee[2])
        print("Department  :", employee[3])
        print("Salary      :", employee[4])


# SEARCH
def search_employee():
    print("\n--- Search Employee ---")

    try:
        emp_id = int(input("Enter Employee ID: "))

        cursor.execute(
            "SELECT * FROM employees WHERE employee_id = ?",
            (emp_id,)
        )

        employee = cursor.fetchone()

        if employee:
            print("--------------------------------")
            print("Employee ID :", employee[0])
            print("Name        :", employee[1])
            print("Designation :", employee[2])
            print("Department  :", employee[3])
            print("Salary      :", employee[4])
        else:
            print("Employee not found.")

    except ValueError:
        print("Invalid Employee ID.")


# UPDATE
def update_employee():
    print("\n--- Update Employee ---")

    try:
        emp_id = int(input("Enter Employee ID: "))

        cursor.execute(
            "SELECT * FROM employees WHERE employee_id = ?",
            (emp_id,)
        )

        employee = cursor.fetchone()

        if employee is None:
            print("Employee not found.")
            return

        name = input("New Name: ")
        designation = input("New Designation: ")
        department = input("New Department: ")
        salary = float(input("New Salary: "))

        cursor.execute(
            """
            UPDATE employees
            SET name = ?,
                designation = ?,
                department = ?,
                salary = ?
            WHERE employee_id = ?
            """,
            (name, designation, department, salary, emp_id)
        )

        conn.commit()
        print("Employee updated successfully.")

    except ValueError:
        print("Invalid input.")


# DELETE
def delete_employee():
    print("\n--- Delete Employee ---")

    try:
        emp_id = int(input("Enter Employee ID: "))

        cursor.execute(
            "SELECT * FROM employees WHERE employee_id = ?",
            (emp_id,)
        )

        employee = cursor.fetchone()

        if employee is None:
            print("Employee not found.")
            return

        answer = input("Delete this employee? (y/n): ")

        if answer.lower() == "y":
            cursor.execute(
                "DELETE FROM employees WHERE employee_id = ?",
                (emp_id,)
            )

            conn.commit()
            print("Employee deleted successfully.")
        else:
            print("Delete cancelled.")

    except ValueError:
        print("Invalid Employee ID.")


# MAIN MENU
def main():
    while True:
        print("\n================================")
        print("    EMPLOYEE MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


main()

# Close database
conn.close()
