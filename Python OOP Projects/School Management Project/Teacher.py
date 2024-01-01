from Person import Person
import random


class Teacher(Person):
    def __init__(self, _name: str, _age: int, _teacher_id: str, courses_taught: list = None):
        """
        Initializes a new instance of the Teacher class.
        :param _name: str - The name of the teacher.
        :param _age: int - The age of the teacher.
        :param _teacher_id: str - The teacher id of the teacher.
        :param courses_taught: list - List of courses taught by the teacher.
        :raises TypeError: If the name is not a string or age is not an integer.
        :raises ValueError: If the age is negative.
        :raises TypeError: If the teacher id is not a string or empty.
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

    def __repr__(self) -> str:
        return f"Teacher(name:{self._name}, age:{self._age}, teacherID:{self._teacherID})"

    @staticmethod
    def generate_teacher_id() -> str:
        length = 9
        random_id = ''.join(random.choice('0123456789') for _ in range(length))
        return random_id

    def enroll_course(self, course):
        ...

    def view_courses_taught(self):
        ...

    @property
    def teacherID(self) -> int:
        return self._teacherID
