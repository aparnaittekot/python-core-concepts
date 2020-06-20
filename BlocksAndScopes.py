x = 1
y = 4

if x < y:
    z = 10  # Variables in python does not have scopes inside blocks. z can be accessed even outside this block.
    print("First condition {}".format(x))


def sample_func():
    print("Inside sample function!")


sample_func()
print("Outside : {}".format(z))

