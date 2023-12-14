from dataclasses import dataclass, field
from time import perf_counter
from typing import Any, Optional, Callable


def benchmark(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        result = func(args, kwargs)
        end_time = perf_counter()
        delta_t = end_time - start_time
        print(f"Time of Execution: {delta_t}")
        return result
    return wrapper


@dataclass
class Stats:
    _age: int
    _gender: str = field(repr=False)
    _height: float = field(repr=False)
    _weight: float = field(repr=False)
    _blood_type: Optional[str] = field(default=None, repr=False)
    _eye_color: Optional[str] = field(default=None, repr=False)
    _hair_color: Optional[str] = field(default=None, repr=False)

    # use __post_init__ function for validation
    def __post_init__(self) -> None:
        self.age = self._age
        self.gender = self._gender
        self.height = self._height
        self.weight = self._weight
        self.blood_type = self._blood_type
        self.eye_color = self._eye_color
        self.hair_color = self._hair_color

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
    def age(self, new_age: int) -> None:
        if not isinstance(new_age, int):
            raise TypeError(f"Expected integer for age, got {type(new_age).__name__}.")
        self._age = new_age

    @gender.setter
    def gender(self, new_gender: str) -> None:
        if not isinstance(new_gender, str):
            raise TypeError(f"Expected string for gender, got {type(new_gender).__name__}.")
        self._gender = new_gender

    @height.setter
    def height(self, new_height: float) -> None:
        if not isinstance(new_height, (float, int)):
            raise TypeError(f"Expected float for height, got {type(new_height).__name__}.")
        self._height = new_height

    @weight.setter
    def weight(self, new_weight: float) -> None:
        if not isinstance(new_weight, (float, int)):
            raise TypeError(f"Expected float for weight, got {type(new_weight).__name__}.")
        self._weight = new_weight

    @blood_type.setter
    def blood_type(self, new_blood_type: str) -> None:
        if not isinstance(new_blood_type, str):
            raise TypeError(f"Expected string for blood type, got {type(new_blood_type).__name__}.")
        self._blood_type = new_blood_type

    @eye_color.setter
    def eye_color(self, new_eye_color: str) -> None:
        if not isinstance(new_eye_color, str):
            raise TypeError(f"Expected string for eye color, got {type(new_eye_color).__name__}.")
        self._eye_color = new_eye_color

    @hair_color.setter
    def hair_color(self, new_hair_color: str) -> None:
        if not isinstance(new_hair_color, str):
            raise TypeError(f"Expected string for hair color, got {type(new_hair_color).__name__}.")
        self._hair_color = new_hair_color


@dataclass
class Address:
    _address_line_1: str = field(repr=False)
    _address_line_2: str = field(repr=False)
    _city: str
    _postal_code: str
    _country: str = field(default='United States')

    def __str__(self) -> str:
        return f"Address(city:{self.city}, postal code:{self.postal_code}, country: {self.country})"

    def __post_init__(self) -> None:
        self.address_line_1 = self._address_line_1
        self.address_line_2 = self._address_line_2
        self.city = self._city
        self.postal_code = self._postal_code
        self.country = self._country

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
    def address_line_1(self, new_address_line_1: str) -> None:
        if not isinstance(new_address_line_1, str):
            raise TypeError(f"Expected string for address line 1, got {type(new_address_line_1).__name__}.")
        self._address_line_1 = new_address_line_1

    @address_line_2.setter
    def address_line_2(self, new_address_line_2: str) -> None:
        if not isinstance(new_address_line_2, str):
            raise TypeError(f"Expected string for address line 2, got {type(new_address_line_2).__name__}.")
        self._address_line_2 = new_address_line_2

    @city.setter
    def city(self, new_city: str) -> None:
        if not isinstance(new_city, str):
            raise TypeError(f"Expected string for city, got {type(new_city).__name__}.")
        self._city = new_city

    @country.setter
    def country(self, new_country: str) -> None:
        if not isinstance(new_country, str):
            raise TypeError(f"Expected string for country, got {type(new_country).__name__}.")
        self._country = new_country

    @postal_code.setter
    def postal_code(self, new_postal_code: str) -> None:
        if not isinstance(new_postal_code, str):
            raise TypeError(f"Expected string for postal code, got {type(new_postal_code).__name__}.")
        self._postal_code = new_postal_code


@dataclass
class Person:
    _name: str
    address: Address
    _email: str
    _phone_number: str
    stats: Stats

    def __post_init__(self) -> None:
        self.name = self._name
        self.email = self._email
        self.phone_number = self._phone_number

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
            raise TypeError(f"Expected string for name, got {type(new_name).__name__}.")
        self._name = new_name

    @email.setter
    def email(self, new_email: str) -> None:
        if not isinstance(new_email, str):
            raise TypeError(f"Expected string for email, got {type(new_email).__name__}.")
        self._email = new_email

    @phone_number.setter
    def phone_number(self, new_phone_number: str) -> None:
        if not isinstance(new_phone_number, str):
            raise TypeError(f"Expected string for phone number, got {type(new_phone_number).__name__}.")
        self._phone_number = new_phone_number


def main() -> None:
    # create a person
    address = Address(
        _address_line_1="",
        _address_line_2="",
        _city='Charlotte',
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

    print(person)
    print(address)


if __name__ == "__main__":
    main()
