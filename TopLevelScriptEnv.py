# Whenever the Python interpreter reads a source file, it does two things:
# it sets a few special variables like __name__, and then
# it executes all of the code found in the file

# Read this - why these variables are required?
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
# https://docs.python.org/3/library/__main__.html
# https://thepythonguru.com/what-is-if-__name__-__main__/
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/

# There is no multi-line comments in Python!

print("before import")
import math  # math = __import__("math")

print("before functionA")


def function_a():
    print("Function A")


print("before functionB")


def function_b():
    print("Function B {}".format(math.sqrt(100)))


print("before __name__ guard")
if __name__ == '__main__':
    function_a()
    function_b()
print("after __name__ guard")

#
# print("before __name__ guard")
# function_a()
# function_b()
# print("after __name__ guard")
