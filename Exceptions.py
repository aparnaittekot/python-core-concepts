import sys  # Get more information for exceptions.


def main():
    try:
        # int('string')
        # 5 / 0
        a = 3
    except ValueError:
        print("ValueError")
    # except ZeroDivisionError:
    #     print("ZeroDivisionError")
    except:
        print(f"Unknown error {sys.exc_info()}")
    else:
        print("executed if no error")


if __name__ == '__main__':
    main()

# You can even throw errors using "raise ... statement"

raise TypeError("sample error")
