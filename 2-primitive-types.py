# Imports math module
import math

print("Hello World!")
x = 1  # integer
a = 1.0  # float

# long string
long_lyrics = """
Baby Girl, what's your name?
Let me talk to you
Let me buy u a drank
"""

# string methods
print(len(long_lyrics))
print(long_lyrics[::-1])
print(long_lyrics.upper())
print(long_lyrics.strip())
print(long_lyrics.replace("L", "R"))
print("drank" in long_lyrics)
print("drink" not in long_lyrics)

# complex numbers
q = 1 + 2j  # a + bi

# Addition
print(9 + 10)

# Subtraction
print(9 - 10)

# Multiplication
print(9 * 10)

# Division for floats
print(9 / 10)

# Division for integers
print(9 // 10)

# Modulo operator (Remainder)
print(9 % 10)

# Exponent
print(9 ** 10)

# Augmented Assignment operator
l = 10
l = l + 3
# or
l += 3
# This is the same in JS as well


# Functions for numbers

# Rounding a number
round(2.9)  # returns 3

# Returns absolute value of argument
abs(-2.9)  # returns 2.9

# Math module
math.ceil(2.2)  # returns 3

# Math module list
# https://docs.python.org/3/library/math.html

# Allows the user to type up their own input
i = input("i: ")
k = int(i) + 1
# you cannot add a string and a number unless you convert them to be of similat types
# "1" + 1

# Type conversion functions

# convert to integer
print(int("4"))
# convert to float
print(float(4))
# convert to boolean
print(bool(4))
# convert to string
print(str(4))

# Formatted strings
print(f"i: {i}, k: {k}")

# Bool goes by truthy and falsy values
# Falsy values include:
# "" (Empty string)
# 0
# None (equivalent to null in JS)

# A negative integer is still considered True
