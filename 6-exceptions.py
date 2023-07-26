# Exceptions
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
