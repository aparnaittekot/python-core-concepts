class Test:
    test1 = 'sample1'
    test2 = 'sample2'

    def first_func(self):
        print("First function")
        print("value of test1 : {} ".format(self.test1))

    def second_func(self):
        print("Second function")
        print("value of test2 : {} ".format(self.test2))


def main():
    sample = Test()
    sample.first_func()
    sample.second_func()


if __name__ == '__main__':
    main()

# Inheritance
# Interator objects
# https://www.w3schools.com/python/python_iterators.asp