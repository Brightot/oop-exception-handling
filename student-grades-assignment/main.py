
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
        print(line)

except FileNotFoundError:
    print("File could not be found.")