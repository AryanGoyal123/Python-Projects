import csv
import os
import json
from Student import Student
from Teacher import Teacher
from Data.DataManager import DataManager


class Registrar:
    """
    This class will serve as a way to interact with all the other class and perform commands. Think of as an admin class for the entire school management system.
    """
    @staticmethod
    def register_student():
        """
        :return: True if student is successfully registered into the system (csv file is updated)
        """
        student_name = input("Please input new student's name: ").strip()
        student_age = input("Please input new student's age: ").strip()
        student_id = Student.studentID_generator()

        student1 = Student(student_name, student_age, student_id)

        # Now we have the new student object, we need to use the DataManager class to update csv


