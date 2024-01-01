from Course import Course
from Student import Student
from Teacher import Teacher
from Data.DataManager import DataManager
from typing import Any, Optional


class School:
    """
    This class will serve as a way to interact with all the other class and perform commands.
    Think of as an admin class for the entire school management system.
    """

    @staticmethod
    def create_csv() -> None:
        DataManager.create_student_csv()
        DataManager.create_teacher_csv()
        DataManager.create_course_csv()

    @staticmethod
    def register_student() -> None:
        student_name = input("Please input new student's name: ").strip()
        student_age = int(input("Please input new student's age: ").strip())
        student_id = Student.generate_student_id()

        # create an instance of Student class
        student = Student(student_name, student_age, student_id)
        DataManager.add_student_csv(student)

    @staticmethod
    def register_teacher() -> None:
        teacher_name = input("Please input new teacher's name: ").strip()
        teacher_age = int(input("Please input new teacher's age: ").strip())
        teacher_id = Teacher.generate_teacher_id()

        # create an instance of Teacher class
        teacher = Teacher(teacher_name, teacher_age, teacher_id)
        DataManager.add_teacher_csv(teacher)

    @staticmethod
    def register_course() -> None:
        course_name = input("Please input new course name: ").strip()
        course_code = int(input("Please input new course code: ").strip())
        course_credits = int(input("Please input new course credit: ").strip())

        # create an instance from Course class
        course = Course(course_code, course_name, course_credits)
        DataManager.add_course_csv(course)

    @staticmethod
    def ask_person_info() -> (str, str):
        search_field = input("Are you searching for a student or teacher?: ").strip()
        if not search_field.isalpha():
            raise ValueError("Search field can only be 'student' or 'teacher'")

        person_name = input("What is the name of this person: ").strip()
        if not person_name.isalpha():
            raise ValueError("Person name can only contain alphabetic characters")
        return search_field, person_name

    @staticmethod
    def get_person_info_name() -> Any:
        search_field, person_name = School.ask_person_info()

        name_search_result = DataManager.name_search(person_name, search_field)

        if name_search_result == 0:
            print("Name not found")
            return 0
        return name_search_result

    @staticmethod
    def ask_person_info_code() -> (str, str):
        search_field = input("Are you searching for a student or teacher?: ").strip()
        if not search_field.isalpha():
            raise ValueError("Can only search for a student or teacher")

        person_id = input("What is the person's ID number: ").strip()
        if not name.isdigit():
            raise ValueError
        return search_field, person_id

    @staticmethod
    def get_person_info_code() -> Optional:
        search_field, person_id = School.ask_person_info_code()
        code_search_result = DataManager.id_search(person_id, search_field)

        if code_search_result == 0:
            print("Name not found")
            return None
        return code_search_result


school = School
# school.create_csv()
# school.register_student()
name, age, id = DataManager.name_search('Aryan', 'student')
print(f"Name: {name}, Age: {age}, ID: {id}")
