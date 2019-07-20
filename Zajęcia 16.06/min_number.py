"""
Get from user 3 numbers, check the min number and print it
"""

def get_min(a, b, c):
    """
    Return smallest number
    :param a: 
    :param b: 
    :param c: 
    :return: 
    """
    if a < b:
        if a < c:
            return a
        else:
            return c
    elif b < c:
        if b < a:
            return b
    else:
        return c


if __name__ == '__main__':
    values = input('Provide 3 numbers: ').split(' ')
    int_values = []
    for x in values:
        if not x.isdigit():
            print('Is no a number')
            break
        int_values.append(int(x))

    if int_values:
        a, b, c = int_values


    print(get_min(a, b, c))
