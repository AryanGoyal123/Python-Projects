# In this file, I'll go over list and dictionary comprehension

# [expression for item in iterable if condition]
squares = [x ** 2 for x in range(10)]

even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
odd_squares = [x ** 2 for x in range(10) if x % 2 != 0]

square_root = [x ** 0.5 for x in range(10)]

# dict comprehension: {key: value for item in iterable if condition}
squares_dict = {x: x ** 2 for x in range(10)}
even_squares_dict = {x: x ** 2 for x in range(10) if x % 2 == 0}
# print(squares_dict)
# print(even_squares_dict)

# using the zip functions for creating a dict from two list
keys = ['a', 'b', 'c']
values = [1, 2, 3]

new_dict = {key: value for key, value in zip(keys, values)}
#
# List Comprehension: Create a list of the first letters of each word in the list ['Hello', 'World', 'Python',
# 'Programming'].
list0 = ['Hello', 'World', 'Python', 'Programming']
list1 = [x[0] for x in list0]

# Conditional List Comprehension: Generate a list of even numbers from 0 to 20, but exclude numbers that are greater
# than 10.
list_02 = [x for x in range(20) if x % 2 == 0 and not x > 10]

# Dictionary Comprehension: Create a dictionary where the keys are numbers from 1 to 5 and the values are their
# respective cubes.
dict_01 = {x: x ** 3 for x in range(1, 6)}

# Nested List Comprehension: Create a flattened list from the nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_03 = [x for sublist in nested_list for x in sublist]

# Dictionary Comprehension with Condition: Make a dictionary from the list ['apple', 'banana', 'cherry'] where the
# fruit names are keys and their lengths are values, but only include fruits with more than 5 characters.
list_04 = ['apple', 'banana', 'cherry']
dict1 = {item: len(item) for item in list_04 if len(item) > 5}
