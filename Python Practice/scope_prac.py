"""In python, there are three types of variable scopes: public, private, and protected
Public variables are easy to understand as they are just regular vars we always use.
Protected variables intended for use within the class and its  subclasses. They are indicated by prefixing the attribute
name with a single underscore (_).
Private variables are designed to not be accessed outside the class,
"""


class MyClass:
    def __init__(self, input1, _input2, __input3):
        self.input1 = input1  # public
        self._input2 = _input2  # protected
        self.__input3 = __input3  # private

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
print(myclass.input1)
print(myclass.input2)  # does not print out, does an Attribute Error because of protection, use the getter function
print(myclass.input3)  # does not print out, use the method to access from inside the class
