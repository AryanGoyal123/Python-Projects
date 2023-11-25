# labda functions
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y

# map functions maps each of the values to the lambda function and then generates a new map object,
# need to convert it back into list type
squared_numbers = map(lambda x: x ** 2, range(5))
print(list(squared_numbers))

input_values = [3, 6, 7, 8, 5, 6, 7, 10, 9]
output_numbers = list(map(lambda x: (x + 5) / 2, input_values))
print(output_numbers)

# filter applies the function to each of the elements in a list and selects the ones that are true
even_numbers = list(filter(lambda x: x % 2 == 0, range(10)))
odd_numbers = list(filter(lambda x: (x % 2 != 0), range(10)))

print(multiply(5, 4))
print(add(10, 20))
print(subtract(50, 10))
