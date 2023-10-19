from Person import Person


class Teacher(Person):
    def __init__(self, name, age, teacher_id, courses_taught=None):
        super().__init__(name, age)

        self.teacherID = teacher_id
        if courses_taught is None:
            """
            load data from CSV file
            """

    def enroll_course(self, course):
        pass

    def view_courses_taught(self):
        pass

    def get_teacher_details(self):
        super().get_person_details()
        print(f"Teacher ID: {self.teacherID}")