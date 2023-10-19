"""
This class will manage read and write to the JSON and CSV Files
We need a CSV file to store the name of student, teachers, and course list
JSON file to store the courses students are enrolled in, and their respective grades
JSOn file to store the courses the teacher is teaching
"""
import csv
import os


class DataManager:
    student_csv_file_path = 'student.csv'
    teacher_csv_file_path = 'teacher.csv'
    courses_csv_file_path = 'courses.csv'

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
    
                # Write data to the CSV file
                writer.writerows(data)

    @classmethod
    def create_teacher_csv(cls):
        pass

    @classmethod
    def create_course_csv(cls):
        pass
