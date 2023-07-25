# Comparison Operators (Used to compare values)

10 > 3  # True
10 >= 3  # True
10 < 20  # True
5 > 10  # False

# In Python, their equality operator is "==" (Double equals)
10 == 10  # True
10 == "10"  # False

# Not Equal
10 != "10"  # True

"bag" > "apple"  # True
"bag" == "BAG"  # False

# Conditional Statements
temperature = 15

if temperature > 30:
    print("It's warm")
    print("Drink water")
# Else If
elif temperature > 20:
    print("It's nice")
# Else (if it doesn't meet two conditions)
else:
    print("It's cold")
print("Done")

# Regular if else statement
age = 19

# if age >= 21:
#     message = "You can go to the casino!"
# else:
#     message = "NOT ALLOWED!"

# Ternary Operator
message = "You can go to the casino!" if age >= 21 else "NOT ALLOWED!"
# If written in JS, age >= 21 ? console.log("You can go to the casino!") : console.log("NOT ALLOWED!")
print(message)

# Logical operators
high_income = True
good_credit = False
student = False

if (high_income or good_credit) and not student:
    print("Eligible for the loan")
else:
    print("Not eligible")

# and (JS: &&)
# or (JS: ||)
# not (JS: !)

# Short circuit evaluation
# Logical operators start from the left side, it continues as long as it returns True, and stops if it runs into False
# If the first evaluation it runs into is False, it will short circuit and stop evaluating the rest of the operators for and operator
# For or operator, it continues and check if either of the operators return True

# Chaining comparison operators
# Age should be between 18 and 25
if 18 <= age < 65:
    print("Eligible")


print("bag" > "cat")

# For loops
for number in range(1, 10, 2):
    print("This is a for loop", number, (number) * ".")

# For else loops
successful = False

for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Failed")

# Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


# Iterables
# for x in range(5):
# The range function returns a range object which can be iterable (we can iterate over it)
# x will have a different vaklue everytime
# Strings are also iterable
for x in "Python":
    print(x)

for x in [1, 2, 3, 4, 5]:
    print(x)

# for item in shopping_cart:
#     print(item)


# While loops
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# Infinite loops
while True:
    command = input(">")
    print("ECHO", command)
    # If statement allows this program to quit, otherwise it loops forever
    if command.lower() == "quit":
        break

# Excerise (Write a program to display the even numbers between 1 to 10)
even_numbers = []
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        even_numbers.append(i)
print(f"We have {len(even_numbers)} even numbers")
