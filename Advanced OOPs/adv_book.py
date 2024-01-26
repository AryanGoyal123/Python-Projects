from dataclasses import dataclass, field
import re
from typing import Optional


@dataclass
class Book:
    title: str
    author: str = field(default="Unknown Author")
    publication_year: Optional[int] = lambda: None
    genre: Optional[str] = lambda: None
    _isbn: str = field(default="Unknown", repr=False)
    _pages: int = field(default=0, compare=False)
    _price: float = field(default=0.0, compare=False)
    _quantity: int = field(default=0, compare=False, repr=False)

    """ __post_init__ is executed after the __init__ method has completed, meaning all the data class fields have 
        already been assigned. Used for validation of different fields. """

    def __post_init__(self) -> None:
        self._validate_fields()

        # validate the isbn and pages instance variables
        self.isbn = self._isbn
        self.pages = self._pages
        self.price = self._price
        self.quantity = self._quantity

    def _validate_fields(self) -> None:
        # validate the title, author, publication and genre (if not none) type
        if not isinstance(self.title, str):
            raise ValueError(f"Expected string for title, got {type(self.title).__name__}")

        if not isinstance(self.author, str):
            raise ValueError(f"Expected string for author, got {type(self.author).__name__}")

        if self.publication_year is not None and not isinstance(self.publication_year, int):
            raise ValueError(f"Expected integer for publication year, got {type(self.publication_year).__name__}")

        if self.genre is not None and not isinstance(self.genre, str):
            raise ValueError(f"Expected string for the genre, got {type(self.genre).__name__}")

    def __str__(self) -> str:
        return f'Book(title={self.title}, author={self.author}, pages={self.pages}, price={self.price})'

    @property
    def isbn(self) -> str: return self._isbn

    @property
    def pages(self) -> int: return self._pages

    @isbn.setter
    def isbn(self, value: str) -> None:
        if not re.match(r"^\d{10}|\d{13}$", value):
            raise ValueError("Invalid ISBN format")
        self._isbn = value

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"Expected integer for pages, got {type(value).__name__}")
        self._pages = value

    @property
    def price(self) -> float: return self._price

    @property
    def quantity(self) -> int: return self._quantity

    @price.setter
    def price(self, new_price: float) -> None:
        if not isinstance(new_price, float) or new_price < 0.0:
            raise ValueError(f"Expected float for price, got {type(new_price).__name__}")
        self._price = new_price

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        if not isinstance(new_quantity, int) or new_quantity < 0:
            raise ValueError(f"Expected integer for quantity, got {type(new_quantity).__name__}")
        self._quantity = new_quantity


@dataclass
class AudioBook(Book):
    _length: float = field(default=0.0, compare=False, metadata={"units": "seconds"})

    def __post_init__(self) -> None:
        # data validation
        super().__post_init__()
        self.length = self._length

    def __str__(self) -> str:
        return f'EBook(title={self.title}, author={self.author}, length={self.length} seconds, price=${self.price})'

    @property
    def length(self) -> float: return self._length

    @length.setter
    def length(self, new_length: float) -> None:
        if not isinstance(new_length, float) or new_length < 0:
            raise ValueError(f"Expected float for length of AudioBook, got {type(new_length).__name__}")
        self._length = new_length


@dataclass
class EBook(Book):
    _size: float = field(default=0.0, compare=False, metadata={"units": "MB"})

    def __post_init__(self) -> None:
        # data validation
        super().__post_init__()
        self.size = self._size

    def __str__(self) -> str:
        return f'EBook(title={self.title}, author={self.author}, size={self.size} MB, price=${self.price})'

    @property
    def size(self) -> float: return self._size

    @size.setter
    def size(self, new_size: float) -> None:
        if not isinstance(new_size, float) or new_size < 0:
            raise ValueError(f"Expected float for length of AudioBook, got {type(new_size).__name__}")
        self._size = new_size


def main():
    ebook = EBook(
        title='Changing World Order',
        _size=14.0,
        _isbn='1234567890',
        _price=9.99
    )

    print(ebook)


if __name__ == "__main__":
    main()
