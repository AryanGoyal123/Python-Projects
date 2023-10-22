import random

from Person import Person
import json


class Student(Person):
    def __init__(self, name, age, student_id, courses_enrolled=None):
        super().__init__(name, age)

        self.studentID = student_id
        if courses_enrolled is None:
            """
            load data from CSV file
            """
            pass

    def enroll_course(self, course):
        pass

    def view_transcript(self):
        pass

    def get_student_details(self):
        super().get_person_details()
        print(f"Student ID: {self.studentID}")

    @classmethod
    def studentID_generator(cls):
        return random.randint(1,100)
