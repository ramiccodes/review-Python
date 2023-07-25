# Lists

from sys import getsizeof
from array import array
from collections import deque

letters = ["a", "b", "c"]
# A matrix is a 2 dimensional list
matrix = [[0, 1], ["a", "b"]]

# If you want to make a list of 5 zeroes, you can:
zeros = [0] * 5

print(zeros)

# You can also concatenate multiple lists by using the "+" operator
combined = zeros + letters

print(combined)

# If you want to have a list of numbers all the way up to 20:
# The list() function takes an iterable, and returns a list
numbers = list(range(20))
print(numbers)

hello = list("Hello World")
print(len(hello))

# Accessing Items
print(letters[1])

# Returns the last item in the list
print(letters[-1])

# You can also change a value in the list:
letters[0] = "z"
print(letters)

# Returns the values in that range
print(letters[0:2])

# Returns all the values in the list
print(letters[0:])

# Defaults to 0 if first range argument not passed in
print(letters[:2])

# You could also pass in a third range argument called step to
# explicitly set how much steps the range should increment
# It returns the value every in every step

print(numbers[::2])

# Returns the list in reverse
print(numbers[::-1])


# List unpacking

# Unpacking way
z, b, c = letters
# This one is exactly identical as the one below

# The caveat to this is the number of variables on the left side of the assignment operator
# must be equal to the amount of items in the list

# It returns an error if it isn't equal

# Standard way
z = letters[0]
print(z)
b = letters[1]
print(b)
c = letters[2]
print(c)

# What is there's a ton of items in a list but we only care
# about the first two?

# We can use the same syntax to specify the first two and the
# pack the rest of the list into a separate list

zero, one, *other = numbers

# The single asterisk syntax is for the variable number of arguments
print(zero)
print(other)

# You can also put the new list in between, not just at the end

# Looping over Lists
for letter in letters:
    print(letter)

# The enumerate function returns an enumerated object, a tuple of the index and the value
for letter in enumerate(letters):
    print(letter[0], letter[1])

# Tuples can also be unpacked, if we do it like this, we don't have to worry
# about indexes to access specific values

# You can directly unpack the tuple returned from enumerate function in the for loop
for index, letter in enumerate(letters):
    print(index, letter)

# Adding or removing items
# Everything in Python is a object, so you can use dot notation to access methods

# Adds an item at the end of the list
letters.append("L")

# Adds an item at a specific location (takes in two arguments, an index and the item)
letters.insert(0, "o")

# Removes items at the end of the list
# You can also pass in an optional argument of an index to remove a specific item from the list
letters.pop(0)

# You can use the remove method to remove a specific item if you do not know its index
# If there's multiple instances of the same item, it removes the first instance
letters.remove("z")

# If you want to remove all instances of an item in the list,
# you'd have to loop over the list and call the method above to remove
# them individually

# Another way to remove an item from the list is by using the del or delete statement
# You can enter it an item by its index or a range of items
# del letters[0:3]

# If you want to remove everything from a list, use the clear() method
# letters.clear()

print(letters)


# Finding items

# Index method takes in an argument of an item and returns its index
# It returns an error if the item is not found, unlike C languages like JavaScript which returns -1
print(letters.index("c"))

# Returns the count of the specific items in the list
letters.count("c")

# Sorting Lists

random_nums = [3, 51, 2, 8, 6]
# Sorts the list in ascending order (lowest to highest)
random_nums.sort()
print(random_nums)
# Passing it a reverse = True arguments sorts the list in descending order (highest to lowest)
random_nums.sort(reverse=True)
print(random_nums)

# We also have a sorted() function, it return a new sorted list, and wouldn't modify the original list
print(sorted(random_nums))

items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 8),
]

# items.sort() wouldn't work for this list, you need to create a separate function


def sort_item(item):
    # This gets the number of a tuple, if you want to sort by the number
    return item[1]


items.sort(key=sort_item)
print(items)

# Now it sorts the tuple based on its integers

# Lambda function (Anonymous function)
# To create a lambda, the format is the keyword lambda parameters:expression
items.sort(key=lambda item: item[1])


# Map Function
# JS Equivalent
# const map1 = array1.map(x => x * 2);
prices = []
x = map(lambda item: item[1], items)

# You can also turn what is returned from the map function into a list by using the list function
prices = list(map(lambda item: item[1], items))

print(prices)

# Filter
filtered = []
y = list(filter(lambda item: item[1] >= 10, items))
print(y)

# List Comprehension
# Comprehension example

# [expression for item in items]
price_comp = [item[1] for item in items]
print(price_comp)
filtered = [item for item in items if item[1] >= 10]
print(filtered)

# Zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# How to combine two lists to be like this?
# [(1,10), (2,20), (3,30)]

# Use the zip function:
print(list(zip(list1, list2)))

# Stacks (LIFO - Last In, First Out)
browsing_session = []
browsing_session.append("google.com")
browsing_session.append("ramiccodes.com")
browsing_session.append("linkedin.com")
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])
browsing_session.pop()
browsing_session.pop()
# if browsing_session is a falsey value (empty list) and not which turns it into True:
if not browsing_session:
    print('back button disabled')

# Queues (FIFO - First In, First Out)
# You can use a stack for this and remove from the first item but for a large list, it will have performance issues
# deque function imported from module above
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")


# Tuples (A read only list)
# You can also exclude the parenthesis and python would still consider it a tuple as long as the comma exists
point = (1, 2) + (3, 4)
print(point)
reverse_point = (4, 3) * 3
print(reverse_point)

# You can also convert a list to a tuple by using the tuple() function
print(tuple([1, 2]))
print(tuple("Hello"))

print(reverse_point[0])

# We can also unpack tuples

# When do we use tuples in the real world?
# You're dealing with a sequence of object and you want to make sure, you don't accidentally
# modify this sequence, you don't accidentally add a new object or remove an existing object.


# Swapping Variables
ten = 10
eleven = 11

ten, eleven = eleven, ten

print(ten)
print(eleven)

# Arrays
# If you're dealing with a large sequence of numbers, we have a more efficient data type in python.
# They take less memory and perform a little bit faster
# array function imported from module above
num_array = array("i", [1, 2, 3])
num_array.append(4)  # or insert or pop or access by index
# The difference between array and list however is that the object inside the array are typed
# If anything other than an integer is appended to this array, it will return an error
# They must be all the same type, as indicated by the type code in the first argument in the array function


# Sets
# (A collection with no duplicates)
# Sets are enclosed in curly brackets
# You can use the methods: add, remove also the len() function
# Sets are UNORDERED unlike lists, so we cannot access them with their index
reverse_letters = ['z', 'y', 'x', 'z']
uniques = set(reverse_letters)
print(uniques)

reverse_num = {10, 9, 8, "z"}

# Vertical bar returns a new set that combined the two sets on the right and left of the vertical bar
print(uniques | reverse_num)
# The ampersand returns a new set with values that the two sets intersect on (where they have the same values)
print(uniques & reverse_num)
# The dash returns a new set with values additional values that the second set doesn't have
print(uniques - reverse_num)
# The ^ returns a new set with values that are either first or second sets but not both
print(uniques ^ reverse_num)

# We can check if a value exists in a set like this:
if 'z' in reverse_letters:
    print("yes")


# Dictionaries
# A collection of key value pairs ( like object in JavaScript)
info = {"x": 1, "y": 2}
# You can also create a dictionary using the function dict()
infos = dict(x=1, y=2)
infos['x'] = 10
infos['z'] = 20
print(infos["y"])
print(infos)

# You cannot access a value of a key that doesn't exist (It will return an error)
# You can check if a key exists in a dictionary like this:
if 'a' in infos:
    print(infos['a'])

# ANother method:
# Passing in a second argument defines what you want it to return as a default if key is not found
print(infos.get('a', 0))

# To delete a key value pair:
del infos['z']
print(infos)

# You can iterate over every key in the dictionary:
for key in infos:
    print(infos[key])

# Another way:
for key, value in infos.items():
    print(key, value)


# Dictionary Comprehension
# Comprehension format:
# [expression for item in items]
dict_comp = {x: x * 2 for x in range(5)}
print(dict_comp)

# Generators
# When you have to store large items in memory, use a generator object
# They are iterable
# They don't store in memory but instead generate or spit out a new value in each iteration
generator_comp = (x * 2 for x in range(5))
print(generator_comp)
for x in generator_comp:
    print(x)

# Comparing the size of a generator and a list
# module: from sys import getsizeof
values = (x * 2 for x in range(100000))
print("Generator:", getsizeof(values), "bytes of memory")
# Even if the range is 1000 or 100000, the size of the generator object remains consistent
# You CAN'T use the len() function on a generator object

# List
values_list = [x * 2 for x in range(100000)]
print("List:", getsizeof(values_list), "bytes of memory")


# Unpacking operator
# * is the unpacking operator, this is equivalent to JavaScript's spread operator (...)
num_range = [1, 2, 3, 4, 5]
print(*num_range)

# We can unpack any iterable, here's making a list using the unpacking operator:
range_five = [*range(5), *"Hello"]
print(range_five)

# You can also combine two lists together using the unpacking operator
combined_list = [*num_range, *range_five, "Yellow"]
print(combined_list)

# Unpacking dictionaries (Use two ** instead of *)
dict_one = {'x': 1}
dict_two = {'x': 10, 'y': 2}
combined_dict = {**dict_one, **dict_two, "j": 0}
print(combined_dict)
# If the dictionaries both have a same key, the value of that key will be from the latter dictionary

print("======================================")
print("PRACTICE EXERCISE")
print("======================================")
# Exercise
# (Write a program that finds the most repeated character in a sentence)
# sentence = "This is a common interview question"
# sentence = "The quick brown lazy fox jumped over the lazy fence"
sentence = "Lucky for you, that's what I like."

# For each character in a sentence, make a key value pair in a dictionary


def find_most_repeated_char(sentence):
    characters = {x: 0 for x in sentence}
    most_repeated = sentence[0]

    for char in sentence:
        if (char in characters) and char != ' ':
            characters[char] += 1

    for char in characters:
        if characters[char] > characters[most_repeated]:
            most_repeated = char

    print(characters)
    print(most_repeated)
    return most_repeated


# dict_comp = {x: x * 2 for x in range(5)}
# print(dict_comp)

# if 'a' in infos:
#     print(infos['a'])

find_most_repeated_char(sentence)
