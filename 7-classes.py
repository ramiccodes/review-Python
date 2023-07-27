# Classes
# - A blueprint for creating new objects
x = 1
print(type(x))  # class int

# Every object that we have in Python is created using a class
# Object - Instance of a class

# Class: Human
# Object: John, Mary, Jack


# Creating Classes
# (Name written is Pascal naming convention - First letter capital)


class Point:
    def draw(self):
        print("draw")

# Every Point object we make now has this draw method


point = Point()
print(type(point))  # class __main__.Point

# isinstance function finds out whether an object is an instance of a given class
print(isinstance(point, Point))
print(isinstance(point, int))

# Constructors
# - A special method that is called when we create a new Point object
# __init__ is a special method called the magic method, this one in particular is called the constructor
# after adding self, we can add extra parameters to the constructor
# self is reference to the current Point object


class PointArgs:
    default_color = "Red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __add__(self, other):
        return PointArgs(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    @classmethod
    def zero(cls):
        cls(0, 0)


point_coordinates = PointArgs(1, 2)
print(point_coordinates.y)
point_coordinates.draw()

# Class vs Instance attributes
# We can also define an attribute after we create the Point object
point_coordinates.z = 10
# The attributes we have defined so far are x, y, and z. They belong to Point instances

another_point = PointArgs(3, 4)
another_point.draw()

# Each point has its own attribute, just like John and Mary can have different eye colors.
# These are instance attributes

# We can also define class attributes. They are attributes that we define at the class level
# and they are the same across all instances of a class

PointArgs.default_color = "Yellow"
# Instance
print(point_coordinates.default_color)
print(another_point.default_color)
# Class
print(PointArgs.default_color)

# Class vs Instance Methods
# A function defined within a class is called a method, which you can call using the dot notation
another_point.draw()  # Instance method
# .zero() is a factory method, because its like a factory, it creates a new
# object
zero = PointArgs.zero()
# When making a factory method, pass it the argument cls (class) instead of the usual self.
# To make it a class method, put @classmethod on top of the defined method, this is called a decorator
# A decorator is a way to extend the behavior of a method or function.
# cls(0, 0) automatically pass a reference to the Point class to the zero method

print(zero)

# Magic Methods
# Methods that have two underscores at the beginning and end
# def __init__ magic method automatically by the python interpreter when
# we create a new Point object

# google search python 3 magic methods

# __str__ (self) - called when we try to convert an object to a string
print(point_coordinates)
# Same result if you did print(str(point_coordinates))


# Comparing Objects
point1 = PointArgs(10, 20)
point2 = PointArgs(1, 2)
print(point1 == point2)
# This returns false because compares the references and addresses of these
# two objects in memory. This is why they're not equal
# We need a magic method to compare two objects

# __eq__ magic method defined above

print(point1 > point2)

# __gt__ magic method defined above

print(point1 < point2)


# Supporting Arithmetic Operations
# We also have magic methods for arithmetic between two objects

# If we want to add these two points together
# Normal arithmetic operations

# __add__ magic method defined above

print(point1 + point2)


# Making custom containers
class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def len(self):
        return len(self.__tags)

    # Makes the class an iterable
    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
# print(cloud.__tags)  # Attribute error: doesn't have __tags


# Private members
# The problem with the class TagCloud above is that it gives us access to
# the underlying dictionary that is used to keep track of the count of text
# To fix this, we need to hide the attribute from the outside, so we cannot
# access it

# On the self.__tags property on the init function, rename __tags to be ____tags
# to make it private

# If you prefix with '__' it makes it private
# You can still access this, however
print(cloud.__dict__)
print(cloud._TagCloud__tags)


# Properties
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = Product(10)
product.price = 20  # Has set_price as property
print(product.price)  # Has get_price as property
# This is not good, the product can't have negative price

# The code above is not "Pythonic", not using Python's best practices
# The implementation above is the kind of code a Java programmer learning Python would write
# In Python, we have a better way to achieve the same result, this is when we use a Property.

# A property is an object that sits in front of an attribute and allows us to get or set the value
# of an attribute and allows us to get or set the value (kind of like in Ruby) of an attribute.

# To define a property: (See above)
# property() function accepts 4 optional arguments:
# 1. function for getting
# 2. function for setting
# 3. function for deleting
# 4. documentation

# For the get and set methods to be hidden, we must use a decorator (see above)
# By using a decorator, we can easily create a property.
# Without making a setter decorator, we'll have a read only property, once it is set
# we cannot change it
