import csv
import os
import json
from Student import Student
from Teacher import Teacher
from Data.DataManager import DataManager


class School:
    """
    This class will serve as a way to interact with all the other class and perform commands.
    Think of as an admin class for the entire school management system.
    """

    @staticmethod
    def create_csv():
        DataManager.create_student_csv()
        DataManager.create_teacher_csv()
        DataManager.create_course_csv()

    @staticmethod
    def register_student():
        """
        :return: True if student is successfully registered into the system (csv file is updated)
        """
        student_name = input("Please input new student's name: ").strip()
        student_age = int(input("Please input new student's age: ").strip())
        student_id = Student.generate_student_id()

        # create an instance from Student class
        student = Student(student_name, student_age, student_id)
        DataManager.add_student_csv(student)


school = School
school.create_csv()
school.register_student()
