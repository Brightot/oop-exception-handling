
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

        try:
            parts = line.strip().split(",")

            student_id = parts[0]
            name = parts[1]
            subject = parts[2]
            grade = parts[3]

            student = Student(student_id, name)

            student.validate_id(student_id)
            grade = student.validate_grade(grade)

            if student_id not in students:
                students[student_id] = student

            students[student_id].add_grade(subject, grade)

        except ValueError:
            print("Problem with line:", line.strip())

        except InvalidIDError:
            print("Invalid student ID:", line.strip())

        except InvalidGradeError:
            print("Invalid grade:", line.strip())

        except IndexError:
            print("Missing data in line:", line.strip())
except FileNotFoundError:
    print("File could not be found.")








