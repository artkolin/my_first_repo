"""
Is leap year
"""

def is_leap(year):
    """
    Return true if year is leap otherwise return false
    :param year:
    :return:
    """
    return (year % 4 == 0) and ((year % 100 == 0) or (year % 400 == 0))

def is_leap_simpler(year):
    """
    Simplier version
    :param year:
    :return:
    """
    if year % 4 == 0:
        if (year % 100 !=0) or (year % 400 == 0):
            return True
    return False

if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))