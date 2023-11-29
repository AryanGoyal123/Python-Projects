"""
In this document, I am re-learning about args anf kwargs
args: are arbitrary arguments passed in as a tuple
kwargs: are arbitrary argument passed in as a dict but have keywords with them
"""


def sum_numbers(*args):
    """
    *args allows a function to take any number of positional arguments.
    It collects extra positional arguments into a tuple.
    Useful when you don't know in advance how many arguments will be passed to your function.
    """
    return sum(args)


def print_numbers(**kwargs):
    """
    **kwargs allows for any number of keyword arguments (arguments specified by name).
    It collects extra keyword arguments into a dictionary.
    Useful for functions that need to handle named arguments dynamically.
    """
    for key, value in kwargs.items():
        print(f"{key}:{value}")


def person_details(**kwargs: str) -> None:
    for key, value in kwargs.items():
        if not isinstance(value, str):
            raise TypeError
        
    name = kwargs['name']
    age = int(kwargs['age'])
    job = kwargs['job']
    print(f'name:{name}, age:{age}, job:{job}')


print_numbers(first=1, second=2)
person_details(name='Aryan', age='19', job='student')

