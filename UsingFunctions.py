#!/usr/bin/env python3

import platform


def main():
    message()


def message():
    print('This is python version : {}'.format(platform.python_version()))


#
if __name__ == '__main__':
    main()


# Providing default values if not passed.

def sample(a=1):
    print(a)


sample()
sample(10)


# Retuning values from a function.
def sample(b=5):
    return b


print(sample())
print(sample(10))


# Use *args for list elements in functions and **kwargs for dict.
# Generators can be used to return multiple values in python : yield is used to return the specific values one by one.
def print_values():
    print("Inside print_values()")
    for i in generated_range(5):
        print(i)


def generated_range(*args):
    start = 0
    args_len = len(args)
    stop = 0
    step = 1

    if args_len == 1:
        stop = args[0]
    elif args_len == 2:
        (start, stop) = args
    elif args_len == 3:
        (start, stop, step) = args

    i = start
    while i <= stop:
        yield i
        i += step


print_values()


# Decorators : returns or pass functions to another function.

def f1(f):
    print("Inside f1()")

    def f3():
        print("Inside f3()")
        f()

    return f3()


@f1
def f2():
    print("Inside f2()")


f2()
