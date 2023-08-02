# Creating Modules
# As our program grows, we should split our code across multiple files
# You call each file a module, and each of them contains Python code
# A module should contain highly related objects, they can be functions, objects, classes, methods, variables etc.

# The code below could be in another file named sales.py
import sys


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


# Module Search Path
# When you import a module, Python will look for it with its name with the .py extension
# If it doesn't find it, it will look in a bunch of the predefined directories that come with Python installation
print(sys.path)
# The list of strings above are the directories that Python will search the modules on
# To import a module from a sub directory, we need to look at Packages


# Packages
# As our programs grow, we're gonna have to organize it into sub directories
# WIthin a new folder, we need to create a new python file names __init__.py
# Adding this file within a folder, Python would treat the folder as a package.
# A package is a container for one or more modules
# For example:
# You create a folder with the name ecommerce and within it the sales.py file
# You need to create __init__.py for python to treat it as a package
# You can then import the specific module within that package using dot notation:
# import <packagename>.<filename>
# import ecommerce.sales

# To invoke a method within that packages:
# <packagename>.<filename>.<method>()
# ecommerce.sales.calc_tax()

# This is tedious
# Better approach is to use the from statement:
# from <packagename>.<filename> import <method>
# from ecommerce.sales import calc_tax
# By doing this, you can call the calc_tax method normally:
# calc_tax()

# What if you want to use multiple objects in the sales module?
# from <packagename> import <filename>
# from ecommerce import sales
# We can then use the dot notation to access all the methods within that file
# sales.calc_tax

# Sub-packages
# For example, our ecommerce package has another package inside it named shopping
# We also have to create a file named __init__.py within that folder to turn it into a
# package
# To import that package:
# from <packagename>.<subpackage.name> import <filename>
# from ecommerce.shopping import sales


# Intra-package References
# There are times you want to import modules from sibling packages, not sub packages
# Alongside ecommerce packages, we add a customer package
# Within that customer package is a contact.py file
# For example, we want to use the contact.py from customer package within our sales file
# You open the sales.py file and within it:
# from ecommerce.customer import contact
#  ^ this is called an absolute import
# You can then invoke the method within it:
# contact.contact_customer()

# from ..customer import contact
#  ^ We can also use a relative import

# As a best practice, prefer to use absolute imports and that's what pep8 also recommends
