
# here I am importing the Student class
from student import Student, InvalidIDError, InvalidGradeError

# dictionary to store all students
# key = student id
# value = student object
students = {}

try:

    # trying to open the grades file
    file = open("grades.txt", "r")

    # reading the file one line at a time
    for line in file:
        parts = line.strip().split(",")

        student_id = parts[0]
        name = parts[1]
        subject = parts[2]
        grade = parts[3]

        print(student_id, name, subject, grade)

except FileNotFoundError:
    print("File could not be found.")








