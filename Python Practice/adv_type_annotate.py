from typing import List, Dict, Tuple, Optional, Union

Vector = List[Union[int, float]]
Matrix = List[List[Union[int, float]]]


# You can use union types to specify that a variable or parameter can have multiple types
def scale_vector(vector: Vector, factor: Union[int, float]) -> Vector:
    return [item * factor for item in vector]


def square_to_double(value: Union[int, float]) -> Union[int, float]:
    return value ** 2 if isinstance(value, (int, float)) else value * 2


def process_items(items: List[int]) -> Dict[str, Tuple[int, int]]:
    result = {}
    for i, item in enumerate(items):
        result[f'item_{i}'] = (item, item * 2)
    return result


# The Optional type annotation is a way to express that a variable argument may be of a certain type or None
def greet(name: Optional[str]) -> str:
    if name is not None:
        return f"Hello, {name}!"
    return "Hello, Guest!"


def find_element(id_list: List[int], target: int) -> Optional[int]:
    if target in id_list:
        return target
    return None
