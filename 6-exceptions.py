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
