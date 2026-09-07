import sqlite3
from pathlib import Path

# Database file
DATABASE = Path("employees.db")


def create_database():
    """Create database tables and insert sample data."""

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()

        # Create departments table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS departments (
                department_id INTEGER PRIMARY KEY,
                department_name TEXT NOT NULL UNIQUE
            )
        """)

        # Create employees table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                employee_id INTEGER PRIMARY KEY,
                employee_name TEXT NOT NULL,
                department_id INTEGER NOT NULL,
                salary REAL NOT NULL CHECK (salary >= 0),
                FOREIGN KEY (department_id)
                    REFERENCES departments(department_id)
            )
        """)

        # Insert departments if table is empty
        cursor.execute("SELECT COUNT(*) FROM departments")

        if cursor.fetchone()[0] == 0:
            departments = [
                (1, "Human Resources"),
                (2, "Finance"),
                (3, "Information Technology"),
                (4, "Sales")
            ]

            cursor.executemany("""
                INSERT INTO departments
                    (department_id, department_name)
                VALUES (?, ?)
            """, departments)

        # Insert employees if table is empty
        cursor.execute("SELECT COUNT(*) FROM employees")

        if cursor.fetchone()[0] == 0:
            employees = [
                (101, "Alice", 1, 55000),
                (102, "Bob", 1, 62000),
                (103, "Charlie", 2, 70000),
                (104, "Diana", 2, 78000),
                (105, "Ethan", 3, 90000),
                (106, "Fiona", 3, 85000),
                (107, "George", 3, 95000),
                (108, "Helen", 4, 60000),
                (109, "Ian", 4, 65000)
            ]

            cursor.executemany("""
                INSERT INTO employees
                    (employee_id, employee_name, department_id, salary)
                VALUES (?, ?, ?, ?)
            """, employees)

        conn.commit()


def get_salary_report(department_id=None, minimum_salary=None):
    """Generate a department-wise salary report."""

    query = """
        SELECT
            d.department_id,
            d.department_name,
            COUNT(e.employee_id) AS employee_count,
            COALESCE(SUM(e.salary), 0) AS total_salary,
            COALESCE(AVG(e.salary), 0) AS average_salary,
            COALESCE(MIN(e.salary), 0) AS minimum_salary,
            COALESCE(MAX(e.salary), 0) AS maximum_salary
        FROM departments AS d
        LEFT JOIN employees AS e
            ON d.department_id = e.department_id
    """

    conditions = []
    parameters = []

    # Parameterized department filter
    if department_id is not None:
        conditions.append("d.department_id = ?")
        parameters.append(department_id)

    # Parameterized salary filter
    if minimum_salary is not None:
        conditions.append("e.salary >= ?")
        parameters.append(minimum_salary)

    # Add WHERE clause if filters exist
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    # Group and sort the results
    query += """
        GROUP BY d.department_id, d.department_name
        ORDER BY d.department_name
    """

    # Execute parameterized query
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute(query, parameters)
        return cursor.fetchall()


def display_report(rows):
    """Display salary report in a table."""

    if not rows:
        print("\nNo matching records found.")
        return

    print("\n")
    print("=" * 115)
    print("             DEPARTMENT-WISE EMPLOYEE SALARY REPORT")
    print("=" * 115)

    print(
        f"{'ID':<5}"
        f"{'Department':<28}"
        f"{'Employees':>10}"
        f"{'Total Salary':>18}"
        f"{'Average':>16}"
        f"{'Minimum':>16}"
        f"{'Maximum':>16}"
    )

    print("-" * 115)

    for row in rows:
        (
            department_id,
            department_name,
            employee_count,
            total_salary,
            average_salary,
            minimum_salary,
            maximum_salary
        ) = row

        print(
            f"{department_id:<5}"
            f"{department_name:<28}"
            f"{employee_count:>10}"
            f"{total_salary:>18,.2f}"
            f"{average_salary:>16,.2f}"
            f"{minimum_salary:>16,.2f}"
            f"{maximum_salary:>16,.2f}"
        )

    print("=" * 115)


def main():
    """Main application."""

    # Create database and sample records
    create_database()

    while True:
        print("\n==============================================")
        print("       EMPLOYEE SALARY REPORT SYSTEM")
        print("==============================================")
        print("1. Show all departments")
        print("2. Show a specific department")
        print("3. Show employees above a minimum salary")
        print("4. Exit")
        print("==============================================")

        choice = input("Enter your choice (1-4): ").strip()

        try:
            if choice == "1":
                # Show all departments
                rows = get_salary_report()
                display_report(rows)

            elif choice == "2":
                # Show specific department
                department_id = int(
                    input("Enter department ID: ").strip()
                )

                rows = get_salary_report(
                    department_id=department_id
                )

                display_report(rows)

            elif choice == "3":
                # Show employees above minimum salary
                minimum_salary = float(
                    input("Enter minimum salary: ").strip()
                )

                if minimum_salary < 0:
                    print("Salary cannot be negative.")
                    continue

                rows = get_salary_report(
                    minimum_salary=minimum_salary
                )

                display_report(rows)

            elif choice == "4":
                print("\nThank you for using the Salary Report System.")
                break

            else:
                print("\nInvalid choice. Please enter 1, 2, 3, or 4.")

        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

        except sqlite3.Error as error:
            print(f"\nDatabase error: {error}")


# Program starts here
if __name__ == "__main__":
    main()
