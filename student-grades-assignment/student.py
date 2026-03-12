
# custom exception for invalid student ID
class InvalidIDError(Exception):
    pass


# custom exception for invalid grade
class InvalidGradeError(ValueError):
    pass

# This class represents a student
class Student:

    # constructor for creating a student object
    def __init__(self, student_id, name):

        # storing the student ID
        self._student_id = student_id

        # storing the student name
        self._name = name

        # dictionary to store subject and grade
        self._grades = {}

    # this method adds a grade for a subject
    def add_grade(self, subject, grade):

        # if subject already exists, do nothing
        if subject in self._grades:
            return False

        # otherwise add the subject and grade
        self._grades[subject] = grade
        return True

    # this method checks if the student ID is valid
    def validate_id(self, student_id):

        # check if ID is missing
        if student_id == "":
            raise ValueError("Student ID missing")

        # check if ID starts with D00
        if not student_id.upper().startswith("D00"):
            raise InvalidIDError("Student ID must start with D00")

    # this method checks if the grade is valid
    def validate_grade(self, grade):

        # try converting grade to a number
        try:
            grade = float(grade)
        except:
            raise InvalidGradeError("Grade must be numeric")

        # check if grade is between 0 and 100
        if grade < 0 or grade > 100:
            raise InvalidGradeError("Grade must be between 0 and 100")

        return grade

    # this method prints student informationss
    def __str__(self):
        return f"{self._student_id} - {self._name} - {self._grades}"