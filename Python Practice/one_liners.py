# read lines of a file into a list in python
lines = [line.strip() for line in open("sample.txt")]
print(lines)

# apply a function to each of the items in a list
doubled_list = list(map(lambda x: x * 2, [1, 2, 3, 4]))
print(doubled_list)

# apply a filter to each of the items in a list
filtered = list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))
print(filtered)

# concatenate into a single string
concatenated_string = ''.join(['Hello', ' ', 'World'])
print(concatenated_string)

list = ['100,000', '110,000', '120,000']
filtered_list = [float(''.join(i.split(','))) for i in list]
print(filtered_list)
