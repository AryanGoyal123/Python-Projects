import csv
import os


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
    def csv_file_exists(file_path):
        return os.path.isfile(file_path)

    @classmethod
    def create_student_csv(cls):

        if not DataManager.csv_file_exists(cls.student_csv_file_path):
            data = [
                ['Name', 'Age', 'StudentID']
            ]

            with open(cls.student_csv_file_path, mode='w', newline='') as file:
                # Define CSV writer
                writer = csv.writer(file)
                writer.writerows(data)

            return True

        return False

    @classmethod
    def create_teacher_csv(cls):
        if not DataManager.csv_file_exists(cls.teacher_csv_file_path):
            data = [
                ['Name', 'Age', 'TeacherID']
            ]

            with open(cls.teacher_csv_file_path, mode='w', newline='') as file:
                # Define CSV writer
                writer = csv.writer(file)
                writer.writerows(data)

    @classmethod
    def create_course_csv(cls):
        if not DataManager.csv_file_exists(cls.courses_csv_file_path):
            data = [
                ['Course Name', 'Course Code', 'Credits']
            ]

            with open(cls.courses_csv_file_path, mode='w', newline='') as file:
                # Define CSV writer
                writer = csv.writer(file)
                writer.writerows(data)

    @classmethod
    def add_student_csv(cls, student):

        # create a new list for the student
        data = [
            [f'{student.name}', f'{student.age}', f'{student.studentID}']
        ]
        if DataManager.csv_file_exists(cls.student_csv_file_path):
            with open(cls.student_csv_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
        else:
            raise FileNotFoundError("Student File Not Found")

    @classmethod
    def add_teacher_csv(cls, teacher):
        # create a new list for the teacher
        data = [
            [f'{teacher.name}', f'{teacher.age}', f'{teacher.teacherID}']
        ]

        if DataManager.csv_file_exists(cls.teacher_csv_file_path):
            with open(cls.teacher_csv_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
        else:
            raise FileNotFoundError("Teacher File Not Found")
