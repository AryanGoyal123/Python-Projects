from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Union


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


@dataclass
class Circle(Shape):
    _diameter: float = field(default=0.0)
    PI = 3.14159

    def __post_init__(self) -> None:
        self.diameter = self._diameter
        self.radius = self._diameter / 2

    def __repr__(self) -> str:
        return f"Circle(diameter={self.diameter}, radius={self.radius})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Circle):
            return False
        return self.diameter == other.diameter

    @property
    def area(self) -> float:
        return (self.radius * self.radius) * Circle.PI

    @property
    def perimeter(self) -> float:
        return 2 * self.radius * Circle.PI

    @property
    def diameter(self) -> float:
        return self._diameter

    @diameter.setter
    def diameter(self, new_diameter: Union[int, float]) -> None:
        if not isinstance(new_diameter, (int, float)):
            raise TypeError(f"Expected float for width, got {type(new_diameter).__name__}.")
        elif new_diameter < 0:
            raise ValueError("Only Positive Values Are Allowed")
        self._diameter = new_diameter


@dataclass
class Rectangle(Shape):
    _width: float = field(default=0.0)
    _height: float = field(default=0.0)

    def __post_init__(self) -> None:
        self.width = self._width
        self.height = self._height

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return ((self.width, self.height) == (other.width, other.height) or
                (self.width, self.height) == (other.height, other.width))

    @property
    def area(self) -> float:
        return self._height * self._width

    @property
    def perimeter(self) -> float:
        return 2 * (self._width + self._height)

    @property
    def width(self) -> float:
        return self._width

    @property
    def height(self) -> float:
        return self._height

    @width.setter
    def width(self, new_width: Union[int, float]) -> None:
        if not isinstance(new_width, (int, float)):
            raise TypeError(f"Expected float for width, got {type(new_width).__name__}.")
        if new_width < 0.0:
            raise ValueError("Only Positive Values Are Allowed")
        self._width = new_width

    @height.setter
    def height(self, new_height: Union[int, float]) -> None:
        if not isinstance(new_height, (int, float)):
            raise TypeError(f"Expected float for height, got {type(new_height).__name__}.")
        if new_height < 0.0:
            raise ValueError("Only Positive Values Are Allowed")
        self._height = new_height


@dataclass
class Square(Rectangle):
    _side: float = field(default=0.0)

    def __post_init__(self) -> None:
        self.width = self.height = self._side

    def __repr__(self) -> str:
        return f"Square(side={self.width})"

    @property
    def side(self) -> float:
        return self._side
