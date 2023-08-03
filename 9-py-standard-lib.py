# Python Standard Library
# Python has a batteries included philosophy which means it comes with a comprehensive
# library of packages and modules that provide common feature that we need when building
# real applications

# We're going to learn how to work with:
# - Files and directories
# - SQLite databases
# - Date/Time
# - Generate Random Values
# - Send emails


# Working with Paths
# We're going to learn how to work with files and directories in Python
# We're going to look at the Path class because that's the foundation to work with
# files and directories
# import pathlib import Path
from pathlib import Path

# We can create an absolute path
# On Mac or Linux:
Path("/usr/local/bin")

# You can also create the Path object that represents the current folder or we can use
# a relative path
Path("python/9-py-standard-lib.py")

# We can also combine Path objects
# You can have one path and then using a slash, combine with another path
Path() / Path("python")

# You can also combine a Path object with a string
Path() / "python" / "7-classes.py"

# We can also get the home directory of the current user
# The Path class has a method called home() that returns the home directory
# of the current user
Path.home()

# Example:
# path = Path("python/__init__.py")
# path.exists() - Checks to see if this file or directory exists or not
# path.is_file() - Checks if this path represents a file (Returns True or False)
# path.is_dir() - Checks if this path represents a directory (Returns True or False)
# path.name - Returns the file name in this path
# path.stem - Returns the file name in this path without the extension
# path.suffix - Returns extension
# path.parent - Returns parent folder
# path.with_name("file.txt")
#   - Create a new path object based on this existing path but only change the name and extension of the file
# path.absolute()
#   - Returns the absolute value of this path
# path.with_suffix(".txt")
#   - Changes the extension of a file
