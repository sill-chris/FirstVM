"""
Object model test scripts
"""


def modify(k):
    """
    Modifes content of my list
    :param k: list
    :return: nothing
    """
    k.append(33)
    print("k= ", k)


def replace(g):
    """
    Replace the content of the list
    :param g: list
    :return: nothing
    """
    g = [17, 36, 22, 33]
    print("g= ", g)


def update_info(h):
    """
    Updates list content by incrementing each member by 1
    :param h: list object
    :return: nothing
    """
    i = 0
    while i < len(h):
        h[i] +=1
        i += 1
        print("h = ", h)


def banner(message, border='*'):
    '''
    Displays message surrounded by border
    :param message: message string <string>
    :param border: border style <char>. Optional with
        default '*'
    :return: nothing
    '''

    # Take into account border plus space on both ends
    line = border * (len(message)+4)
    print(line)
    print(border, message, border)
    print(line)


def number_info():
    """
    Write a function that prompts the user
    for two integer then it prints:  The sum,
    the difference, the product, the average,
    and the distance(absolute value), the maximum,
    the minimum
    :return: nothing
    """

    no_one = int(input("Enter 1st integer: "))
    no_two = int(input("Enter 2nd integer: "))

    print("%-12s%5d" % "Sum: ", no_one + no_two)
    print("%-12s%5d" % "Difference: ", no_one - no_two)
    print("%-12s%5d" % "Product: ", no_one * no_two)
    print("%-12s%5d" % "Average: ", (no_one + no_two)/2)
    print("%-12s%9.2d" % "Sum: ", no_one + no_two)


def main():
    """
    Dummy testing function
    :return: nothing
    """
    # m = [9, 12, 45]
    # print("Before m= ", m)
    # modify(m)
    # print("After m= ", m)
    # replace(m)
    # print("After Replace m = ", m )
    # update_info(m)
    # print("After update_info m = ", m )

    # Set parameters in order
    # banner("Hello", '*')
    # Use only required parameters
    # banner("WSU")
    # Use parameters by name
    # banner(border='@', message="Weber State")

    number_info()

    # When are default arguments evaluated

    # Always use immutable objects as integer
    # or strings for default values


def add_spam(menu=None):
    """
    Add spam to my list
    :param menu: Optional list object
    :return: menu
    """
    if menu is None:
        menu = []
    menu.append("spam")
    return menu


if __name__ == '__main__':
    main();