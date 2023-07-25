# Functions

def print_even():
    even_numbers = []
    for i in range(1, 10):
        if i % 2 == 0:
            print(i)
            even_numbers.append(i)
    print(f"We have {len(even_numbers)} even numbers")


print_even()

# Functions arguments


def multiplication_table(num, max):
    print(f"This is the multiplication table of {num}, {max} times")
    for i in range(1, max + 1):
        print(f"{num} x {i} = {num * i}")
        print("==========================")


multiplication_table(6, 12)

# Keyword arguments


def increment(num, by):
    return num + by


print(increment(2, by=1))

# Default arguments


def increment_def(num, by=1):
    return num + by


print(increment_def(2))
# It's ok to pass one argument if there is already a default value for the other arguments

# xargs
# If you wanted to pass in a variable number of arguments (many arguments)
# Square brackets = Lists
# Parenthesis = Tuples

# The diffrence between them is unlike Lists, we cannot modify Tuples but we can still iterate over them


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 4, 5, 6))

# xxargs
# When double asterisks are used, we can pass multiple key value pairs to the function
# Which Python will packaged into a dictionary, and you can access a value by accessing the key


def save_user(**user):
    print(user["name"])


save_user(id=1, name="John", age=22)
# This creates key value pairs, In Python it is called a Dictionary
# (Javascript is Objects)

# Scope
# Talks about blocks and the scope of variables and values
# Local variables can't be accessed in the global scope
# But Global variables can be accessed anywhere

# Debugging


# Mac VSCode Tricks
# To jump to the end of the line, hold the function key (fn) and press
# the right arrow key
# If going to the left, fn + left arrow key
# If going to top or end of the file, fn + up or down arrow key

# Exercise
# If input is divisible by 3: print Fizz
# If input is divisible by 5: print Buzz
# If input is divisible by 3 and 5: print FizzBuzz
# If input is not divisible by 3 and 5: print current number
def fizz_buzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    print(num)


fizz_buzz(103)
