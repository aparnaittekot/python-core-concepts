#!/usr/bin/env python3  => Shebang line!

import platform

# .format() provides way to give place holders.
print('This is python version {}'.format(platform.python_version()))

# You can also give multiple placeholders with .format()
print('This is python version {} and compiler {}'.format(platform.python_version(), platform.python_compiler()))

# You can also give multiple placeholders with .format()
print('This is python version {} and sample value : {}'.format(platform.python_version(), 12))

# This is the deprecated version of '.format' for string objects. It might be removed in the later versions of python.
x = 14
print('Hello world : %d' % x)

# You can use the above statement in the format manner as follows:
print(f'Hello world with format f : {x}')

# Print the values in single line.
numbers = [1, 4, 7, 2, 7]
for i in numbers:
    print(i, end=' ', flush=True)
