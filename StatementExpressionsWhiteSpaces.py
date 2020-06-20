import platform
import math  # math = __import__("math")

version = platform.python_version()

print('The python version is : {}'.format(version))
print('The end')


# Statements are usually written in separate lines. These are never written in a single line.

def function_a():
    print("Function A")


def function_b():
    print("before functionB")
    print("Function B {}".format(math.sqrt(100)))
    if True:
        print(12)


# Functions are given proper indentation so that it looks more cleaner. The associated statements for the functions
# are written within the blocks.

print("before __name__ guard")
if __name__ == '__main__':
    function_a()
    function_b()
print("after __name__ guard")
