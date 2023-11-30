from Course import Course
from Student import Student
from Teacher import Teacher
from Data.DataManager import DataManager


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

        # create an instance from Student class
        student = Student(student_name, student_age, student_id)
        DataManager.add_student_csv(student)

    @staticmethod
    def register_teacher() -> None:
        teacher_name = input("Please input new teacher's name: ").strip()
        teacher_age = int(input("Please input new teacher's age: ").strip())
        teacher_id = Teacher.generate_teacher_id()

        # create an instance from Teacher class
        teacher = Teacher(teacher_name, teacher_age, teacher_id)
        DataManager.add_student_csv(teacher)

    @staticmethod
    def register_course() -> None:
        course_name = input("Please input new course name: ").strip()
        course_code = int(input("Please input new course code: ").strip())
        course_credits = int(input("Please input new course credit: ").strip())

        # create an instance from Course class
        course = Course(course_code, course_name, course_credits)
        DataManager.add_course_csv(course)


school = School
# school.create_csv()
# school.register_student()
name, age, id = DataManager.name_search('Aryan', 'student')
print(f"Name: {name}, Age: {age}, ID: {id}")
