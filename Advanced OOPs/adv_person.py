from dataclasses import dataclass, field
from time import perf_counter
from typing import Any


def benchmark(func):
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        result = func(args, kwargs)
        end_time = perf_counter()
        delta_t = end_time - start_time

        print(f"Time of Execution: {delta_t}")

        return result
    return wrapper()


@dataclass
class Stats:
    _age: int
    _gender: str
    _height: float
    _weight: float
    _blood_type: str
    _eye_color: str
    _hair_color: str

    # use __post_init__ function for validation
    # def __post_init__(self) -> None:
    #     self.age = self._age
    #     self.gender = self._gender
    #     self.height = self._height
    #     self.weight = self._weight
    #     self.blood_type = self._blood_type
    #     self.eye_color = self._eye_color
    #     self.hair_color = self._hair_color

    # calculate the BMI of a person
    @property
    def bmi(self) -> float:
        return self._weight / (self._height ** 2)

    @property
    def bmi_category(self) -> str:
        bmi_value = self.bmi
        if bmi_value < 18.5:
            return "Underweight"
        elif bmi_value < 25:
            return "Normal"
        elif bmi_value < 30:
            return "Overweight"
        return "Obese"

    @property
    def age(self) -> int:
        return self._age

    @property
    def gender(self) -> str:
        return self._gender

    @property
    def height(self) -> float:
        return self._height

    @property
    def weight(self) -> float:
        return self._weight

    @property
    def blood_type(self) -> str:
        return self._blood_type

    @property
    def eye_color(self) -> str:
        return self._eye_color

    @property
    def hair_color(self) -> str:
        return self._hair_color

    @age.setter
    def age(self, new_age: int):
        if not isinstance(new_age, int):
            raise ValueError
        self._age = new_age

    @gender.setter
    def gender(self, new_gender: str):
        if not isinstance(new_gender, str):
            raise TypeError
        self._gender = new_gender

    @height.setter
    def height(self, new_height: float):
        if not isinstance(new_height, float):
            raise TypeError
        self._height = new_height

    @weight.setter
    def weight(self, new_weight: float):
        if not isinstance(new_weight, float):
            raise TypeError
        self._weight = new_weight

    @blood_type.setter
    def blood_type(self, new_blood_type: str):
        if not isinstance(new_blood_type, str):
            raise TypeError
        self._blood_type = new_blood_type

    @eye_color.setter
    def eye_color(self, new_eye_color: str):
        if not isinstance(new_eye_color, str):
            raise TypeError
        self._eye_color = new_eye_color

    @hair_color.setter
    def hair_color(self, new_hair_color: str):
        if not isinstance(new_hair_color, str):
            raise TypeError
        self._hair_color = new_hair_color


@dataclass
class Address:
    _address_line_1: str
    _address_line_2: str
    _city: str
    _postal_code: str
    _country: str = field(default='United States')

    def __str__(self) -> str:
        return f"{self._address_line_1}, {self._address_line_2}, {self._city}, {self._country}, {self._postal_code}"

    @property
    def address_line_1(self) -> str:
        return self._address_line_1

    @property
    def address_line_2(self) -> str:
        return self._address_line_2

    @property
    def city(self) -> str:
        return self._city

    @property
    def country(self) -> str:
        return self._country

    @property
    def postal_code(self) -> str:
        return self._postal_code

    @address_line_1.setter
    def address_line_1(self, new_address_line_1: str):
        if not isinstance(new_address_line_1, str):
            raise ValueError
        self._address_line_1 = new_address_line_1

    @address_line_2.setter
    def address_line_2(self, new_address_line_2: str):
        if not isinstance(new_address_line_2, str):
            raise ValueError
        self._address_line_2 = new_address_line_2

    @city.setter
    def city(self, new_city: str):
        if not isinstance(new_city, str):
            raise ValueError
        self._city = new_city

    @country.setter
    def country(self, new_country: str):
        if not isinstance(new_country, str):
            raise ValueError
        self._country = new_country

    @postal_code.setter
    def postal_code(self, new_postal_code: str):
        if not isinstance(new_postal_code, str):
            raise ValueError
        self._postal_code = new_postal_code


@dataclass
class Person:
    _name: str
    address: Address
    _email: str
    _phone_number: str
    stats: Stats

    def split_name(self) -> tuple[str, str]:
        first_name, second_name = self._name.split(' ')
        return first_name, second_name

    def __str__(self) -> str:
        return f"Person(name: {self._name}, email: {self._email}, phone number: {self._phone_number})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise ValueError
        self._name = new_name

    @email.setter
    def email(self, new_email: str) -> None:
        if not isinstance(new_email, str):
            raise ValueError
        self._email = new_email

    @phone_number.setter
    def phone_number(self, new_phone_number: str) -> None:
        if not isinstance(new_phone_number, str):
            raise ValueError
        self._phone_number = new_phone_number


def main() -> None:
    # create a person
    address = Address(
        _address_line_1="",
        _address_line_2="",
        _city=123,
        _country="USA",
        _postal_code="12345",
    )
    stats = Stats(
        _age=30,
        _gender="Male",
        _height=1.8,
        _weight=90,
        _blood_type="B+",
        _eye_color="Black",
        _hair_color="Black",
    )
    person = Person(
        _name="Aryan Goyal",
        _email="aryanlovesmath@gmail.com",
        _phone_number="704-456-7890",
        address=address,
        stats=stats,
    )



if __name__ == "__main__":
    main()
