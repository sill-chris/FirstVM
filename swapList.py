def swap(val):
    """
    Swap the first half with the second half
    :param val: a list of objects
    :return: new order list
    """
    pass
    temp = val[4:]
    val[3:] = val[:4]
    val[:3] = temp


def main():
    val = [9, 13, 21, 4, 11, 7, 1, 3]
    print(val)
    swap(val)
    print(val)

if __name__ == '__main__':
    main()
