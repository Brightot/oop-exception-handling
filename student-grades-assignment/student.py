
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