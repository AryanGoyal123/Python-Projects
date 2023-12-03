from dataclasses import dataclass, field
import re


@dataclass
class Product:
    _price: float = field(default=0.0, compare=False)
    _quantity: int = field(default=0, compare=False, repr=False)

    @property
    def price(self) -> float:
        return self._price

    @property
    def quantity(self) -> int:
        return self._quantity

    @price.setter
    def price(self, new_price: float):
        if not isinstance(new_price, float) or new_price < 0.0:
            raise ValueError
        self._price = new_price

    @quantity.setter
    def quantity(self, new_quantity: int):
        if not isinstance(new_quantity, int) or new_quantity < 0:
            raise ValueError
        self._quantity = new_quantity


@dataclass
class Book(Product):
    title: str
    author: str = field(default="Unknown Author")
    _isbn: str = field(default="Unknown", repr=False)
    _pages: int = field(default=0, compare=False)

    """
        __post_init__ is executed after the __init__ method has completed, 
        meaning all the data class fields have already been assigned.
        Used for validation of different fields
    """

    def __post_init__(self) -> None:

        # validate the title and author type
        if not isinstance(self.title, str):
            raise ValueError(f"Expected string for title, got {type(self.title).__name__}")
        if not isinstance(self.author, str):
            raise ValueError(f"Expected string for author, got {type(self.author).__name__}")

        # validate the isbn and pages instance variables
        self.isbn = self._isbn
        self.pages = self._pages

    def __str__(self) -> str:
        return f'Book(title={self.title}, author={self.author}, pages={self._pages}, price={self.price})'

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def pages(self) -> int:
        return self._pages

    @isbn.setter
    def isbn(self, value: str) -> None:
        if not re.match(r"^\d{10}|\d{13}$", value):
            raise ValueError("Invalid ISBN format")
        self._isbn = value

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("Pages must be an positive integer.")
        self._pages = value


def main():
    book1 = Book(title="Changing World Order", author="Ray Dalio",
                 _isbn='1234567890', _pages=340)

    book2 = Book(title="Changing World Order", author="Ray Dalio",
                 _isbn='1234567890', _pages=350)
    print(book1)
    print(book2)
    print(book1 == book2)


if __name__ == "__main__":
    main()
