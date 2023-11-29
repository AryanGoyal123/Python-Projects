from dataclasses import dataclass


@dataclass
class Stats:
    _age: int
    _gender: str
    _height: float
    _weight: float
    _blood_type: str
    _eye_color: str
    _hair_color: str

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


@dataclass
class Address:
    _address_line_1: str
    _address_line_2: str
    _city: str
    _country: str
    _postal_code: str

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
    def address_line_1(self, new_address_line_1):
        if not isinstance(new_address_line_1, str):
            raise ValueError
        self._address_line_1 = new_address_line_1

    @address_line_2.setter
    def address_line_2(self, new_address_line_2):
        if not isinstance(new_address_line_2, str):
            raise ValueError
        self._address_line_2 = new_address_line_2

    @city.setter
    def city(self, new_city):
        if not isinstance(new_city, str):
            raise ValueError
        self._city = new_city

    @country.setter
    def country(self, new_country):
        if not isinstance(new_country, str):
            raise ValueError
        self._country = new_country

    @postal_code.setter
    def postal_code(self, new_postal_code):
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
    def name(self, new_name) -> None:
        if not isinstance(new_name, str):
            raise ValueError
        self._name = new_name

    @email.setter
    def email(self, new_email) -> None:
        if not isinstance(new_email, str):
            raise ValueError
        self._email = new_email

    @phone_number.setter
    def phone_number(self, new_phone_number) -> None:
        if not isinstance(new_phone_number, str):
            raise ValueError
        self._phone_number = new_phone_number


def main() -> None:
    # create a person
    address = Address(
        _address_line_1="",
        _address_line_2="",
        _city="Charlotte",
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
