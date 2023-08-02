# Creating Modules
# As our program grows, we should split our code across multiple files
# You call each file a module, and each of them contains Python code
# A module should contain highly related objects, they can be functions, objects, classes, methods, variables etc.

# The code below could be in another file named sales.py
def calc_tax():
    pass


def calc_shipping():
    pass

# To import a module:
# from <filename> import <function>
# from sales import calc_shipping

# we can then use the imported function in order code
# To import multiple functions, you can use a comma
# from sales import calc_shipping, calc_tax

# There's also a shortcut to import multiple objects, using an asterisk
# WHile it makes your code shorter, it is bad practice, because in that module you could have
# several different functions or variables, and if yoyu blindly import them into the current module,
# some of those objects may overwrite the objects with the same name in the current module, so don't import all
# objects using the asterisk:
# from sales import *

# Only import the stuff you need.
# There's also a different way to import a module
# import <filename>
# you can then use the filename with the dot notation to access objects within it.
# functions inside that module can now be methods
# Example:
# import sales
# sales.calc_tax()

# You can import the entire module or import specific objects


# Compiled Python Files
# When a file with imported modules is ran, it creates a folder named __pycache__, in this folder, you have the compiled version
# of the module imported into the program. eg. compiled version of sales.py
# The reason Python stores the compiled files in this stored folder is to speed up module loading
# So the next time we run the program, python will look in the compiled folder and if we do have compiled version
# of the sales module, python will simply load up the compiled version
# This results in faster loading of the module, NOT the overall performance of the program
# It automatically recompiles the module if the module is updated
