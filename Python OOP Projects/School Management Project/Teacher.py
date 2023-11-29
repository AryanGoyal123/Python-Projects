from Person import Person


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

    def __str__(self):
        return f"Teacher(name:{self._name}, age:{self._age}, teacherID:{self._teacherID})"

    def enroll_course(self, course):
        pass

    def view_courses_taught(self):
        pass

    @property
    def teacherID(self):
        return self._teacherID
