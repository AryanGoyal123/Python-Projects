from Data import DataManager


class Person:
    def __init__(self, _name: str, _age: int):
        if not isinstance(_name, str):
            raise TypeError("Input Name as String")
        else:
            self._name = _name
        if not isinstance(_age, int):
            raise TypeError("Input Age as Integer")
        else:
            if _age >= 0:
                self._age = _age
            else:
                raise ValueError("Age less than 0")

    def __str__(self):
        return f"Person(name:{self._name}, age:{self._age})"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age: int):
        if not isinstance(new_age, int):
            raise TypeError("Input Age as Integer")
        else:
            if new_age >= 0:
                self._age = new_age
            else:
                raise ValueError("New Age less than 0")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if not isinstance(new_name, str):
            raise TypeError("Name should be a String")
        else:
            self._name = new_name

