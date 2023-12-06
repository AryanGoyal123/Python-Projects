from Person import Person
import random


class Teacher(Person):
    def __init__(self, _name: str, _age: int, _teacher_id: int, courses_taught=None):
        """
        Initializes a new instance of the Student class.
        :param _name: str - The name of the student.
        :param _age: int - The age of the student.
        :param _teacher_id: int - The student id of the student
        :raises TypeError: If the name is not a string or age is not an integer.
        :raises ValueError: If the age is negative.
        :raises TypeError: If the teacher id is not an integer or negative.
        """

        super().__init__(_name, _age)

        if not isinstance(_teacher_id, int) or _teacher_id <= 0:
            raise TypeError("Student ID should be an integer and positive")
        else:
            self._teacherID = _teacher_id

        if courses_taught is None:
            """
            load data from CSV file
            """

    def __str__(self) -> str:
        return f"Teacher(name:{self._name}, age:{self._age}, teacherID:{self._teacherID})"

    def __repr__(self) -> str:
        return f"Teacher(name:{self._name}, age:{self._age}, teacherID:{self._teacherID})"

    @staticmethod
    def generate_teacher_id() -> int:
        characters = '0123456789'
        length = 9

        # Randomly choose characters from the characters list and join them into a string
        random_id = ''.join(random.choice(characters) for _ in range(length))
        return int(random_id)

    def enroll_course(self, course):
        pass

    def view_courses_taught(self):
        pass

    @property
    def teacherID(self) -> int:
        return self._teacherID
