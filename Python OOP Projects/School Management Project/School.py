import os
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

    @staticmethod
    def register_teacher():
        teacher_name = input("Please input new teacher's name: ").strip()
        teacher_age = int(input("Please input new teacher's age: ").strip())
        teacher_id = Teacher.generate_teacher_id()

        # create an instance from Teacher class
        teacher = Teacher(teacher_name, teacher_age, teacher_id)
        DataManager.add_student_csv(teacher)


school = School
school.create_csv()
school.register_student()
