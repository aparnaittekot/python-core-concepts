print("""

This is a string object!!!!

""")


class SampleStringClass(str):
    def __str__(self):
        return self[::-1]


a = SampleStringClass('Sample string')
print(a)

print('Hello world '.upper())
print('Hello world '.lower())
print('hello world '.capitalize())
print('hello world '.title())
print('HeLlO WorLd '.swapcase())

print('HeLlO WorLd '.casefold())
