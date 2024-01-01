class Course:
    def __init__(self, _course_code: int, _course_name: str, _course_credit: int):
        """
        Initializes a new instance of the Student class.
        :param _code: int - The code of the course.
        :param _name: str- The name of the course.
        :param _credit: int - The credit of the course.
        :raises ValueError: If the code is not an integer or is negative.
        :raises ValueError: If the credits is not an integer or is negative.
        :raises TypeError: If the name is not a string.
        """

        self.course_code = _course_code
        self.course_credits = _course_credit
        self.course_name = _course_name
    
    def __repr__(self) -> str:
        return f'Course(name:{self._course_name}, code:{self._course_code}, credits:{self._credits})'

    def add_student(self, student):
        ...

    def remove_student(self, student):
        ...

    def get_course_details(self):
        ...

    @property
    def course_code(self) -> int:
        return self._course_code

    @property
    def course_credits(self) -> int:
        return self._credits

    @property
    def course_name(self) -> str:
        return self._course_name

    @course_code.setter
    def course_code(self, new_course_code: int) -> None:
        """Sets the course's code with value validation."""
        if not isinstance(new_course_code, int) or new_course_code <= 0:
            raise ValueError("Course code should be a positive integer")
        self._course_code = new_course_code

    @course_credits.setter
    def course_credits(self, new_credits: int) -> None:
        """Sets the course's credits with value validation."""
        if not isinstance(new_credits, int):
            raise TypeError("Course code should be a positive integer")
        if not 0 <= new_credits <= 4:
            raise ValueError("Course credit value can only be between 0 and 4")
        self._credits = new_credits

    @course_name.setter
    def course_name(self, new_course_name: str) -> None:
        """Sets the course's name with type validation."""
        if not isinstance(new_course_name, str):
            raise TypeError("Course name should be a string")
        self._course_name = new_course_name
