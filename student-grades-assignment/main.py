

# here I am importing the Student class and the custom exceptions
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

            # removing spaces and splitting the line
            parts = line.strip().split(",")

            # getting the values from the line
            student_id = parts[0]
            name = parts[1]
            subject = parts[2]
            grade = parts[3]

            # creating a student object
            student = Student(student_id, name)

            # checking if the id is valid
            student.validate_id(student_id)

            # checking if the grade is valid
            grade = student.validate_grade(grade)

            # if student not already stored, add them
            if student_id not in students:
                students[student_id] = student

            # adding the subject grade
            students[student_id].add_grade(subject, grade)

        # if something is wrong with the line
        except ValueError:
            print("Problem with line:", line.strip())

        except InvalidIDError:
            print("Invalid student ID:", line.strip())

        except InvalidGradeError:
            print("Invalid grade:", line.strip())

        except IndexError:
            print("Missing data in line:", line.strip())

    # closing the file after reading
    file.close()

# if the file does not exist
except FileNotFoundError:
    print("File could not be found.")


# asking the user to enter a student ID
search_id = input("Enter student ID to search: ")

# checking if the student exists in the dictionary
if search_id in students:

    # if found, print the student information
    print("Student found:")
    print(students[search_id])

else:
    # if not found, print message
    print("No student found with that ID.")