# Student Record Management System

students = []
while True:
    print("1. Insert \n2. Delete \n3. Search \n4. Display \n5. Exit") 
    choice = input("Enter your choice: ")
    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        students.append({
            "Roll": roll,
            "Name": name,
            "Course": course
        })
        print("Student added successfully!")
    elif choice == "2":
        roll = input("Enter Roll No to delete: ")
        found = False
        for student in students:
            if student["Roll"] == roll:
                students.remove(student)
                found = True
                print("Student record deleted.")
                break
        if not found:
            print("Student not found.")
    elif choice == "3":
        roll = input("Enter Roll No to search: ")
        found = False
        for student in students:
            if student["Roll"] == roll:
                print("\nStudent Found:")
                print(student)
                found = True
                break
        if not found:
            print("Student not found.")
    elif choice == "4":
        if students:
            print("\nStudent Records:")
            for student in students:
                print(student)
        else:
            print("No records available.")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")