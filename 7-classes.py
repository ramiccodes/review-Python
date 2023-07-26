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

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


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
