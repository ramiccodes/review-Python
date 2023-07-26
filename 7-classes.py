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
