from Data import DataManager


class Person:
    def __init__(self, _name: str, _age: int):
        """
        Initializes a new instance of the Person class.
        :param _name: str - The name of the person.
        :param _age: int - The age of the person.
        :raises TypeError: If the name is not a string or age is not an integer.
        :raises ValueError: If the age is negative.
        """
        self._name = _name  # this will call the setter method
        self._age = _age

    def __str__(self):
        return f"Person(name:{self._name}, age:{self._age})"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age: int):
        """Sets the person's age with value validation."""
        if not isinstance(new_age, int):
            raise TypeError("Age must be an integer")
        if new_age < 0:
            raise ValueError("Age cannot be negative")
        self._age = new_age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        """Sets the person's name with value validation."""
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        self._name = new_name
