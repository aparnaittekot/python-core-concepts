from decimal import *

a = 6
print(type(a))

a = 6.0
print(type(a))

# No difference between single quotes or double quotes in python.
a = '6'
b = "8"
# Multi line string
c = """ 
5656
"""
# Multi line string
d = '''
23434
'''
print(type(a))
print(type(b))
print(type(c))
print(type(d))

a = True
print(type(a))

a = None
print(type(a))

# For decimals, always use decimal modules for more accuracy.
s = 0.1 + 0.1 + 0.1 - 0.3
print(s)

# Decimal gives precision errors
# https://stackoverflow.com/questions/7545015/can-someone-explain-this-0-2-0-1-0-30000000000000004
# https://en.wikipedia.org/wiki/IEEE_754-1985
# https://stackoverflow.com/questions/56947/how-is-floating-point-stored-when-does-it-matter/57031#57031

first = Decimal('.1')
second = Decimal('.2')
print(first + second)

# List items : Mutable sequence.

x = [1, 2, 3, 6, 7, 3]
x[1] = 10
for i in x:
    print("Value of i : {}".format(i))

# Set items : Immutable sequence.
x = {1, 2, 3, 6, 7, 3}
# x[1] = 10
for i in x:
    print("Value of i : {}".format(i))

# Tuple : Immutable sequence. (This is favoured over List type since it's immutable.)
x = (1, 5, 2, 10, 30)
# x[2] = 123  => YOU CANNOT CHANGE TUPLE'S VALUES!
for i in x:
    print("Value of i : {}".format(i))

# Range : Immutable.
x = range(3)  # You can use this function either as range(end), range(start, end) or range(start, end, step).
for i in x:
    print("Value of i : {}".format(i))

# Convert range to list.
x = list(x)

# Dictionary : Key-Value pairs : These are mutable objects.
x = {'first': 1, 'second': 2, 'third': 3}
x['second'] = 2.0
for k, v in x.items():
    print("Value of key : {}, value : {}".format(k, v))

# type() and id()
x = (1, '2', 3.0, [4, 'four'])
y = (1, '2', 3.0, [4, 'four'])

# Two tuples with same values will not be same. Because they are different objects!
print(id(x))
print(id(y))

if x is not y:
    print("not same!")

# Objects with same values are referenced, so the below two objects are same.
print(id(x[0]))
print(id(y[0]))

if x[0] is y[0]:
    print("same!")

# How to check if its a tuple or something? Use isinstance().
print(isinstance(x, tuple))

list_sample = [1, 3]
print(isinstance(list_sample, list))
