import random
from Person import Person


class Student(Person):
    def __init__(self, _name: str, _age: int, _student_id: str, courses_enrolled=None):
        """
        Initializes a new instance of the Student class.
        :param _name: str - The name of the student.
        :param _age: int - The age of the student.
        :param _student_id: int - The student id of the student
        :raises TypeError: If the name is not a string or age is not an integer.
        :raises ValueError: If the age is negative.
        :raises TypeError: If the student id is not an integer or negative.
        """

        super().__init__(_name, _age)

        if not isinstance(_student_id, int) or _student_id <= 0:
            raise TypeError("Student ID should be an integer and positive")
        else:
            self._studentID = _student_id

        if courses_enrolled is None:
            """
            load data from CSV file
            """
            pass

    def __repr__(self) -> str:
        return f"Student(name:{self._name}, age:{self._age}, studentID:{self._studentID})"

    @staticmethod
    def generate_student_id() -> str:
        length = 9
        random_id = ''.join(random.choice('0123456789') for _ in range(length))
        return random_id

    def enroll_course(self, course):
        ...

    def view_transcript(self):
        ...

    @property
    def studentID(self):
        return self._studentID

