"""
Get "centered average"
"""

def centered_average(nums):
    """
    Return centered average
    :param nums:
    :return:
    """
    sorted_nums = sorted(nums)
    sliced_nums = sorted_nums[1:-1]

    return sum(sliced_nums) // len(sliced_nums)


if __name__ == "__main__":
    test1 = [1, 2, 3, 4, 100]
    print(test1, "->", centered_average(test1), ) # 3

    test2 = [1, 1, 5, 5, 10, 8, 7]
    print(test2, "->", centered_average(test2), ) # 5

    test3 = [1000, 0, 1, 99]
    print(test3, "->", centered_average(test3), ) # 50
