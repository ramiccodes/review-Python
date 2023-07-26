# Exceptions
from timeit import timeit
numbers = [1, 2]
# print(numbers[3])

# An exception is an error that terminates the execution of the program

age = int(input("Age: "))
# The code above throws an exception when passed a string because it cannot
# convert it into an integer

# Handling exceptions
# We need to put the statement above on a try block

try:
    age = int(input("Age: "))
except ValueError as ex:
    print("Please enter a valid age")
    print(ex)
    print(type(ex))
else:
    print("Didn't trigger the except block")
print("Still running")

# When Python sees a try block, it will excecute everything within it
# If for some reason it gives out an error, the code within the except
# block would run

# By doing this, our program wouldn't crash
# (Like try..catch in JavaScript)

# You can also chain an else block after except to run code after it
# if it doesn't trigger the exception block

# We can also optionally define a variable that will include details about
# the exception, mostly the error message and sometimes additional arguments


# Handling different exceptions
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Please enter a valid age")
else:
    print("Didn't trigger the except block")
print("Still running")

# If the example above is passed a 0 for its input,
# it will return a ZeroDivisionError, because we cannot divide a number
# by 0. However, we don't have a matching except clause (ValueError)
# To solve this:
# We add a second except clause
# But, you can also pass two except clauses in a single line
# Whenever Python code is ran and comes across an except clause,
# that one is executed but the other clauses are ignored

# Cleaning Up
# For example we open a file using the open() function, but put the
# close() function that resolves it after the code that throws an exception,
# It will never clean itself up because the code will jump to the except block
# To solve this, we can add a finally clause, which will always be executed,
# regardless if the try block throws an exception or not. This ensures that
# everything is cleaned up

# The With Statement
# with open("app.py") as file
# The code format above allows the code to automatically call file.close() whether we have a finally
# clause or not

# Raising exceptions
# you can also raise or throw exceptions in your own code

# the raise keyword allows us to throw exceptions


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# Doing this is costly however, there is a better way


# The cost of raising exceptions
# from timeit module imported above
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)

if xfactor == None:
    pass
"""

# THe keyword argument number can be set to the number of times we want to execute this piece of code
# It will return the execution time of this piece of code after 10,000 repititions
print("First code", timeit(code1, number=10000))
print("Second code", timeit(code2, number=10000))

# Code 2 have faster execution time because it didn't raise any exceptions
# When developing an app with small user base, it wouldn't matter if you raise exceptions
# But for large scale app, this can severely affect performance

# Raise exceptions when you have to
