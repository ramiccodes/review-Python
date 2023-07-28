# Classes
# - A blueprint for creating new objects
from abc import ABC, abstractmethod
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


# Inheritance
# As you build various classes, they may have one or more features or functions in common
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):  # Inheritance in Action, we say that the Mammal class is an Animal so it inherits all the methods of the animal class
    # Animal: Parent, Base
    # Mammal: Child, Subclass

    def __init__(self):
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
f = Fish()
f.eat()
# Defining a shared method between classes separately is bad for debugging if one of the methods have a bug on them, you got to fix single method
# instance in each class

# Programming Concept: DRY (Don't Repeat Yourself)

# Inheritance is the mechanism that allows us to define the common behavior or functions in one class
# and inherit them from other classes

# We can also inherit the attributes of a base class (See above)
print(m.age)
print(f.age)


# The Object Class
# Couple of useful built in funcitons

# Tells us if object is an instance of a specified Class
print(isinstance(m, Mammal))

# All parent classes inherit from another class called object, even though not included (base class)
print(isinstance(m, object))

# object() is a built in function for creating a new instance an empty object
o = object()

# issubclass() a built in function to see if a class is a subclass of another class
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))


# Method Overriding
# What if we want to add a constructor to the Mammal class and initialize its weight
# (see above)

print(m.age)  # no attribute 'age'?
print(m.weight)

# This is because the Animal class constructor did not execute, but got replaced by Mammal class'
# constructor, which only specifies the weight
# This is called Method Overriding, we are overriding or replacing a method in the base class

# To still initialize the age within the Mammal class, we can use the built in function, super()
# This gives us access to the super or base class, which is the Animal in this case
# super().__init__() (see above)
# This jumps back to the base class and does its constructors first before returning to the the second
# constructor

# We can also change the order, if you want to initialize the Mammal class before the ANimal class
# by putting the super() method at the end of the init of Mammal


# Multi-level Inheritance
# Too much inheritance between classes can increase complexity and introduce various kinds of issues
class Bird(Animal):
    def fly(self):
        print('fly')


class Chicken(Bird):
    pass

# The Chicken class inherits all the features of the bird class, but a chicken cannot fly
# This is an example of inheritance abuse. Another example is concept of employees

# The methods you add in your classes are there to solve a business problem. That is a focus of your software
# If you want to use inheritance, limit it to one or two levels


# Multiple Inheritance
# In Python, a class can have multiple base classes

class Rooster(Bird, Chicken):
    pass

# Similar to Multi level inheritance, this is a source of a lot of issues
# If you don't use it properly, you're going to introduce a lot of bugs in
# your program

# On classes with multiple base class inheritance with the same methods,
# the first base class gets priority when calling a method.
# For example, the Bird class takes precedence when calling a method it shares
# with the Chicken class

# The process looks like this:
# - The python interpreter checks if method exists in the Rooster class
# - If not found, it looks for the method in the Bird class
# - It finds the method in the Bird class
# - It executes it

# This is dangerous because a programmer can change the order of the classes
# and the program would break

# You'll end up with classes that inherit features that they shouldn't

# Multiple inheritance is not always a bad thing, it's bad if not used properly.
# If the base classes provided have nothing in common and you want to inherit
# their features in a separate class, then it's perfectly fine to use
# multiple inheritance

# Multiple inheritance starts to become complicated when the base classes
# have methods in common

# Here's an example of a good inheritance:

# Any object that knows how to fly


class Flyer:
    def fly(self):
        pass


# Any object that knows how to swim

class Swimmer:
    def swim(self):
        pass

# The two classes above are very small and abstract
# They have nothing in common
# We now can combine the features of these two classes:


class FlyingFish(Flyer, Swimmer):
    pass


# A Good Example of inheritance
# Create custom exception called InvalidOperationError
class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


# Stream is the base class which the subclasses FileStream and NetworkStream
# inherit methods from


# Abstract base classes
# There are a few problems with the implemenation above:

stream = Stream()
stream.open()
# Why is this an issue? Because this Stream class is an abstract concept
# What does it mean to "open" a stream? What kind of stream?

# We shouldn't be able to directly to create an instance of the Stream class
# We should always subclass it and then create an instance of the subclass
# We only made the Stream class as a base class to provide some code that we're
# going to reuse across different kinds of streams
# This is the first issue

# The second issue is if you look at File and Network Stream implementation,
# you can see that they both have the same read method
# If we decide to make a new Stream, we must remember to implement the read
# method
# There is no way to enforce a common interface amongst different streams
# It would be nice to have a common interface across these streams

# How can we solve these problems?
# This is when we can use an abstract base class
# It's purpose is to provide some common code to these derivatives. So we want
# to make this Stream class an abstract base class.

# import abc module, which stands for abstract base class
# from abc import ABC, abstractmethod
# defined above
# abstractmethod is a decorator

# To make a class abstract, it should be derived from the ABC
# Stream(ABC)
# Second step is to define common interface for all streams (read method)

# define a read method on the Stream class, and add @abstractmethod decorator
# on the top

# When a class has an abstract method, it's considered an abstract class,
# so we cannot create an instance of them

# Second problem solution
