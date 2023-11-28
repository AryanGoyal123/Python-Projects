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

    """
    Notes: Use protected methods because use can use them in the main and child classes. 
        They also allow getter and setter methods and can be checked for type and other formatting when changed 
    """

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
    def __init__(self, age=0):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("Value Error")

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            raise ValueError("Value Error")

    def get_age(self):
        return self.__age


# try:
#     person = Person(25)  # Initialize with a valid age
#     person.set_age(30)  # Set a new valid age
#     print(person.get_age())  # Access and print the age
#
#     person.set_age(-5)  # Attempt to set a negative age - should raise an error
# except ValueError as e:
#     print(e)

class Rectangle:
    def __init__(self, _width: int, _height: int):

        if not isinstance(_width, int) or not isinstance(_height, int):
            raise TypeError("Input Integer Values")

        if _width >= 0 and _height >= 0:
            self._width = _width
            self._height = _height
        else:
            raise ValueError("Only Positive Values Are Allowed")

    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height}"

    def area(self):
        return self._height * self._width

    def perimeter(self):
        return 2*(self._width + self._height)

    def set_width(self, new_width):
        if not isinstance(new_width, int):
            raise TypeError("Input Integer Values")
        else:
            if new_width >= 0:
                self._width = new_width
            else:
                raise ValueError("Only Positive Values Are Allowed")

    def set_height(self, new_height):
        if not isinstance(new_height, int):
            raise TypeError("Input Integer Values")
        else:
            if new_height >= 0:
                self._height = new_height
            else:
                raise ValueError("Only Positive Values Are Allowed")

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self._width * self._width

    def perimeter(self):
        return 4 * self._width

    def __str__(self):
        return f"Square(side={self._width}"
