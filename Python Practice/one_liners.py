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

list1 = ['100,000', '110,000', '120,000']
filtered_list = [float(''.join(i.split(','))) for i in list1]
print(filtered_list)

names = ["Alice", "Bob", "Eve", "Ian", "Olivia", "Uma", "Yves"]
vowels = ('A', 'E', 'I', 'O', 'U')

vowel_names = list(map(lambda x: x.upper(), filter(lambda name: name[0].upper() in vowels, names)))
non_vowel_names = list(map(lambda x: x.upper(), filter(lambda name: name[0].upper() not in vowels, names)))
print(vowel_names)
print(non_vowel_names)

# Word Length Dictionary: Write a one-liner that takes a sentence, splits it into words, and creates a dictionary
# where each word is a key, and its value is the length of the word.
sentence = 'Write a one-liner that takes a sentence and splits it into words and creates a dictionary'
word_dict = {key: len(key) for key in list(sentence.split(' '))}
print(word_dict)

# Sum of Squares: Given a list of numbers, use map and
# lambda to create a new list where each number is replaced by the square of the number,
# and then find the sum of these squares.
list_of_number = [1, 2, 3, 4, 5, 6, 7, 8]
sum_square_list = sum([num ** 2 for num in list_of_number])
print(sum_square_list)

# Conditional List Comprehension: Given a list of integers, create a new list using a list comprehension
# that contains the square of the integer if the integer is even, and the cube if it is odd.
new_list = list(map(lambda num: num ** 2 if num % 2 == 0 else num ** 3, list_of_number))
new_list2 = [num ** 2 if num % 2 == 0 else num ** 3 for num in list_of_number]
# print(new_list)
# print(new_list2)

# String Transformation: Given a sentence, use map and lambda functions to
# create a new string where each word is reversed, and then join these words back into a sentence.
sentence = 'Write a one-liner that takes a sentence and splits it into words and creates a dictionary'
reverse_word = ' '.join((map(lambda word: word[::-1], sentence.split())))
print(reverse_word)

# Composite Function Application: Create a composite function using map and filter that first filters out all negative
# numbers from a list, and then applies a given function (e.g., square root) to the remaining numbers.
list_num = [4, -5, 7, -6, 3, 2, 1, -4, -7, -8, 9, 5]
positive_sqrt_num = list(
    map(lambda num: round(num ** 0.5, 4), filter(lambda num: True if num >= 0 else False, list_num)))
print(positive_sqrt_num)