"""In python, there are three types of variable scopes: public, private, and protected
Public variables are easy to understand as they are just regular vars we always use.
Protected variables intended for use within the class and its subclasses. They are indicated by prefixing the attribute
name with a single underscore (_).
Private variables are designed to not be accessed outside the class,
"""


class MyClass:
    def __init__(self, input1, _input2, __input3):
        self.input1 = input1  # public
        self._input2 = _input2  # protected
        self.__input3 = __input3  # private

    """ Notes: Use protected methods because use can use them in the main and child classes. 
        They also allow getter and setter methods and can be checked for type and other formatting when changed """

    @property
    def input2(self):
        return self._input2

    @property
    def input3(self):
        return self.__input3

    @input2.setter
    def input2(self, new_input2):
        self._input2 = new_input2

    @input3.setter
    def input3(self, new_input3):
        self.__input3 = new_input3


myclass = MyClass(1, 2, 3)


# print(myclass.input1)
# print(myclass.input2)  # does not print out, does an Attribute Error because of protection, use the getter function
# print(myclass.input3)  # does not print out, use the method to access from inside the class

# Practice Question 1
class Person:
    def __init__(self, age: int) -> None:
        self._age = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0 or not isinstance(new_age, int):
            raise ValueError("Value Error")
        self._age = new_age


class Rectangle:
    def __init__(self, _width: int, _height: int) -> None:
        self._width = _width
        self._height = _height

    def __str__(self) -> str:
        return f"Rectangle(width={self._width}, height={self._height})"

    def __repr__(self) -> str:
        return f"Rectangle(width={self._width}, height={self._height})"

    def __eq__(self, other) -> bool:
        return self.width == other.width and self.height == other.height

    @property
    def area(self) -> float:
        return self._height * self._width

    @property
    def perimeter(self) -> float:
        return 2 * (self._width + self._height)

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @width.setter
    def width(self, new_width: int) -> None:
        if not isinstance(new_width, int):
            raise TypeError(f"Expected integer for width, got {type(new_width).__name__}.")
        if new_width <= 0:
            raise ValueError("Only Positive Values Are Allowed")
        self._width = new_width

    @height.setter
    def height(self, new_height: int) -> None:
        if not isinstance(new_height, int):
            raise TypeError(f"Expected integer for height, got {type(new_height).__name__}.")
        if new_height <= 0:
            raise ValueError("Only Positive Values Are Allowed")
        self._height = new_height


class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side, side)

    def __str__(self) -> str:
        return f"Square(side={self.width})"

    def __repr__(self) -> str:
        return f"Square(side={self.width})"

    def __eq__(self, other) -> bool:
        return self.width == other.width

    @property
    def area(self) -> float:
        return self.width * self._width

    @property
    def perimeter(self) -> float:
        return 4 * self.width


rect = Rectangle(_width=5, _height=10)
rect2 = Rectangle(_width=5, _height=10)

square1 = Square(side=5)
square2 = Square(side=5)
print(square1 == square2)
