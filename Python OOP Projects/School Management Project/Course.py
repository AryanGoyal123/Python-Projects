
class Course:
    def __init__(self, course_code, course_name, credit, student_enrolled, teachers):
        self.student_enrolled = student_enrolled
        self.course_code = course_code
        self.credits = credit
        self.course_name = course_name
        self.teachers = teachers

    def add_student(self, student):
        pass

    def remove_student(self, student):
        pass

    def get_course_details(self):
        pass
