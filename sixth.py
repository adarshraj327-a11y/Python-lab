# Program to read student marks, calculate result, and save it to a new file

f1 = open("students.txt", "r")
f2 = open("result.txt", "w")

for line in f1:
    data = line.split()

    roll = data[0]
    name = data[1]

    m1 = int(data[2])
    m2 = int(data[3])
    m3 = int(data[4])

    total = m1 + m2 + m3
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"

    f2.write(roll + " " + name + " " +
             "Total: " + str(total) +
             " Average: " + str(round(average, 2)) +
             " Grade: " + grade + "\n")

f1.close()
f2.close()

print("Results saved in result.txt")