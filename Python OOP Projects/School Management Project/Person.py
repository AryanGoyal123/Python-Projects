from typing import Callable, Any
from time import perf_counter


def benchmark(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        result = func(args, kwargs)
        end_time = perf_counter()
        delta_t: float = end_time - start_time
        print(f"Time of Execution: {delta_t}")
        return result
    return wrapper


class Person:
    def __init__(self, _name: str, _age: int):
        """
        Initializes a new instance of the Person class.
        :param _name: str - The name of the person.
        :param _age: int - The age of the person.
        :raises TypeError: If the name is not a string or age is not an integer.
        :raises ValueError: If the age is negative.
        """
        self.name = _name  # this will call the setter method
        self.age = _age

    def __repr__(self) -> str:
        return f"Person(name:{self.name}, age:{self.age})."

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        """Sets the person's age with value validation."""
        if not isinstance(new_age, int):
            raise TypeError(f"Expected integer for age, got {type(new_age).__name__}")
        if not (5 <= new_age <= 99):
            raise ValueError("Age cannot be less than 5 or more than 99")
        self._age = new_age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Sets the person's name with value validation."""
        if not isinstance(new_name, str):
            raise TypeError(f"Expected string for name, got {type(new_name).__name__}")
        self._name = new_name
