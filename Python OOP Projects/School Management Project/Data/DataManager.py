import csv
import os
from time import perf_counter
from typing import Any, Optional, Callable, Union


def benchmark(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        delta_t: float = end_time - start_time
        print(f"Time of Execution: {delta_t}")
        return result

    return wrapper


class DataManager:
    """ This class will manage read and write to CSV Files.
        We need a CSV file to store the name of student, teachers, and course list. """

    student_csv_file_path = 'Data/student.csv'
    teacher_csv_file_path = 'Data/teacher.csv'
    courses_csv_file_path = 'Data/courses.csv'

    @staticmethod
    def csv_file_exists(file_path) -> bool:
        return os.path.isfile(file_path)

    @classmethod
    def create_csv(cls, file_path: str, header: list) -> None:
        """ Creates a new CSV file with the specified header if the file does not exist."""
        if not DataManager.csv_file_exists(file_path):
            data = [header]

            with open(file_path, mode='w', newline='') as file:
                # Define CSV writer
                writer = csv.writer(file)
                writer.writerows(data)

    @classmethod
    def create_student_csv(cls) -> None:
        header = ['Name', 'Age', 'StudentID']
        cls.create_csv(cls.student_csv_file_path, header)

    @classmethod
    def create_teacher_csv(cls) -> None:
        header = ['Name', 'Age', 'TeacherID']
        cls.create_csv(cls.teacher_csv_file_path, header)

    @classmethod
    def create_course_csv(cls) -> None:
        header = ['Course Name', 'Course Code', 'Credits']
        cls.create_csv(cls.courses_csv_file_path, header)

    @classmethod
    def add_to_csv(cls, data, file_path) -> None:
        """ Adds data to a CSV file based on the input data from student, teacher, or course."""
        if DataManager.csv_file_exists(file_path):
            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
        else:
            raise FileNotFoundError(f"File Not Found at {file_path}")

    @classmethod
    def add_student_csv(cls, student) -> None:
        data = [f'{student.name}', f'{student.age}', f'{student.studentID}']
        cls.add_to_csv(data, cls.student_csv_file_path)

    @classmethod
    def add_teacher_csv(cls, teacher) -> None:
        data = [f'{teacher.name}', f'{teacher.age}', f'{teacher.teacherID}']
        cls.add_to_csv(data, cls.teacher_csv_file_path)

    @classmethod
    def add_course_csv(cls, course) -> None:
        data = [f'{course.name}', f'{course.code}', f'{course.credits}']
        cls.add_to_csv(data, cls.courses_csv_file_path)

    @classmethod
    def _search_entity(cls, file_path: str, key: Union[int, str], col_index: int) -> Optional[str, str, str]:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            for row in reader:
                if key == int(row[col_index]) or key == row[col_index]:
                    return row[0], row[1], row[col_index]
        return None

    @classmethod
    def search_entity_by_name(cls, name: str, entity_type: str) -> Optional[str, str, str]:
        file_path = cls.teacher_csv_file_path if entity_type == 'teacher' else cls.student_csv_file_path
        return cls._search_entity(file_path, name, 0)

    @classmethod
    def search_entity_by_id(cls, entity_id: int, entity_type: str) -> Optional[str, str, str]:
        file_path = cls.teacher_csv_file_path if entity_type == 'teacher' else cls.student_csv_file_path
        return cls._search_entity(file_path, entity_id, 2)

    @classmethod
    def search_course_by_code(cls, code: int) -> Optional[str, str, str]:
        return cls._search_entity(cls.courses_csv_file_path, code, 1)
