class Course:
    def __init__(self, _code: int, _name: str, _credit: int):
        self._course_code = _code
        self._credits = _credit
        self._course_name = _name

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
        if not isinstance(new_course_code, int) or new_course_code <= 0:
            raise ValueError("Course code should be a positive integer")
        self._course_code = new_course_code

    @credits.setter
    def credits(self, new_credits: int):
        if not isinstance(new_credits, int) or new_credits <= 0:
            raise ValueError("Course code should be a positive integer")
        self._credits = new_credits

    @name.setter
    def name(self, new_course_name: str):
        if not isinstance(new_course_name, str):
            raise TypeError("Course name should be a string")
        self._course_name = new_course_name
