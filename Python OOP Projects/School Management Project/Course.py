class Course:
    def __init__(self, _code: int, _name: str, _credit: int):
        """
        Initializes a new instance of the Student class.
        :param _code: int - The code of the course.
        :param _name: str- The name of the course.
        :param _credit: int - The credit of the course.
        :raises ValueError: If the code is not an integer or is negative.
        :raises ValueError: If the credits is not an integer or is negative.
        :raises TypeError: If the name is not a string.
        """

        self._course_code = _code
        self._credits = _credit
        self._course_name = _name

    def __str__(self) -> str:
        return f'Course(name:{self._course_name}, code:{self._course_code}, credits:{self._credits})'

    def add_student(self, student):
        pass

    def remove_student(self, student):
        pass

    def get_course_details(self):
        pass

    @property
    def code(self):
        return self._course_code

    @property
    def credits(self):
        return self._credits

    @property
    def name(self):
        return self._course_name

    @code.setter
    def code(self, new_course_code: int):
        """Sets the course's code with value validation."""
        if not isinstance(new_course_code, int) or new_course_code <= 0:
            raise ValueError("Course code should be a positive integer")
        self._course_code = new_course_code

    @credits.setter
    def credits(self, new_credits: int):
        """Sets the course's credits with value validation."""
        if not isinstance(new_credits, int) or new_credits < 0:
            raise ValueError("Course code should be a positive integer")
        if not 0 <= new_credits <= 4:
            raise ValueError("Course credit value can only be between 0 and 4")
        self._credits = new_credits

    @name.setter
    def name(self, new_course_name: str):
        """Sets the course's name with type validation."""
        if not isinstance(new_course_name, str):
            raise TypeError("Course name should be a string")
        self._course_name = new_course_name
