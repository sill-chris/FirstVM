"""
Test Exceptions in python
"""
import sys
from math import log


def convert(s):
    """
    Convert to an integer
    :param s: object to convert
    :return: integer object
    :raise: ValueError, TypeError
    """

    try:
        return int(s)
    except (ValueError, TypeError):
        print("Conversion failed: {}".format(str(e),
              file=sys.stderr))
        raise # re-raising the error
        return -1


def string_log(s):
    try:
        v = convert(s)
        return log(v)
    except (ValueError):
        print("Log conversion failed")
        return -1


def main():
    #  i = convert(55)
    #  print(i)
    #  i = convert("55")
    #  print(i)
    #  i = convert("hello")
    #  print(i)
    #  i = convert(1, 2, 3)
    #  print(i)
    i = string_log(55)
    print(i)
    i = string_log("Hello")
    print(i)

if __name__ == '__main__':
    main()
