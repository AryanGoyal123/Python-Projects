import csv
import os
from time import perf_counter
from typing import Any


def benchmark(func):
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        delta_t = end_time - start_time

        print(f"Time of Execution: {delta_t}")
        return result
    return wrapper


class DataManager:
    """
    This class will manage read and write to the JSON and CSV Files
    We need a CSV file to store the name of student, teachers, and course list
    JSON file to store the courses students are enrolled in, and their respective grades
    JSOn file to store the courses the teacher is teaching
    """

    student_csv_file_path = 'Data/student.csv'
    teacher_csv_file_path = 'Data/teacher.csv'
    courses_csv_file_path = 'Data/courses.csv'

    @staticmethod
    def csv_file_exists(file_path) -> bool:
        return os.path.isfile(file_path)

    @classmethod
    def create_student_csv(cls) -> None:

        if not DataManager.csv_file_exists(cls.student_csv_file_path):
            data = [
                ['Name', 'Age', 'StudentID']
            ]

            with open(cls.student_csv_file_path, mode='w', newline='') as file:
                # Define CSV writer
                writer = csv.writer(file)
                writer.writerows(data)

    @classmethod
    def create_teacher_csv(cls) -> None:
        if not DataManager.csv_file_exists(cls.teacher_csv_file_path):
            data = [
                ['Name', 'Age', 'TeacherID']
            ]

            with open(cls.teacher_csv_file_path, mode='w', newline='') as file:
                # Define CSV writer
                writer = csv.writer(file)
                writer.writerows(data)

    @classmethod
    def create_course_csv(cls) -> None:
        if not DataManager.csv_file_exists(cls.courses_csv_file_path):
            data = [
                ['Course Name', 'Course Code', 'Credits']
            ]

            with open(cls.courses_csv_file_path, mode='w', newline='') as file:
                # Define CSV writer
                writer = csv.writer(file)
                writer.writerows(data)

    @classmethod
    def add_student_csv(cls, student) -> None:

        # create a new list for the student
        data = [f'{student.name}', f'{student.age}', f'{student.studentID}']

        if DataManager.csv_file_exists(cls.student_csv_file_path):
            with open(cls.student_csv_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
        else:
            raise FileNotFoundError("Student File Not Found")

    @classmethod
    def add_teacher_csv(cls, teacher) -> None:
        # create a new list for the teacher
        data = [f'{teacher.name}', f'{teacher.age}', f'{teacher.teacherID}']

        if DataManager.csv_file_exists(cls.teacher_csv_file_path):
            with open(cls.teacher_csv_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
        else:
            raise FileNotFoundError("Teacher File Not Found")

    @classmethod
    def add_course_csv(cls, course) -> None:
        # create a new list for the course
        data = [f'{course.name}', f'{course.code}', f'{course.credits}']

        if DataManager.csv_file_exists(cls.courses_csv_file_path):
            with open(cls.courses_csv_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
        else:
            raise FileNotFoundError("Course File Not Found")

    # method to search for a specific student, teacher, or course based on the name
    @classmethod
    @benchmark
    def name_search(cls, name: str, search_field: str):
        if search_field == 'teacher':
            file = cls.teacher_csv_file_path
        elif search_field == 'student':
            file = cls.student_csv_file_path
        else:
            raise ValueError("Wrong search field!")

        """
        Open the given file in read mode and search through the 'Name' Column
        based on the 'name' argument
        """
        with open(file, mode='r', newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)

            for row in reader:
                if name == row[0]:
                    return row[0], row[1], row[2]
                return 0

    # method to search for a specific student or teacher based on the code
    @classmethod
    def id_search(cls, id: int, search_field: str):
        if search_field == 'teacher':
            file = cls.teacher_csv_file_path
        elif search_field == 'student':
            file = cls.student_csv_file_path
        else:
            raise ValueError("Wrong search field!")

        """
        Open the given file in read mode and search through the 'ID' Column
        based on the 'id' argument
        """
        with open(file, mode='r', newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)

            for row in reader:
                if id == row[2]:
                    return row[0], row[1], row[2]
                return 0

    @classmethod
    def course_search(cls, code: int):
        file = cls.courses_csv_file_path

        with open(file, mode='r', newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)

            for row in reader:
                if code == row[1]:
                    return row[0], row[1], row[2]
                return 0
