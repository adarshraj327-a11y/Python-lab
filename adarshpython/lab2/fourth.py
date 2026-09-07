# Student Course Enrollment Analysis

# Student details stored as tuples
student1 = ("1", "Sam")
student2 = ("2", "Bobby")

# Courses stored as sets
courses_Sam = {"Python", "Math", "Physics"}
courses_Bobby = {"Python", "Chemistry", "Math"}

print("Student 1:", student1)
print("Student 2:", student2)

print("\nAll Courses (Union):")
print(courses_Sam | courses_Bobby)

print("\nCommon Courses (Intersection):")
print(courses_Sam & courses_Bobby)

print("\nCourses only Sam has (Difference):")
print(courses_Sam - courses_Bobby)

print("\nCourses only Bobby has (Difference):")
print(courses_Bobby - courses_Sam)