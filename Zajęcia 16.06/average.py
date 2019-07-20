"""
Calculating average
"""

def average_from_list(list):
    sorted_data = sorted(list)
    needed_numbers = sorted_data[1:len(sorted_data)-1]
    sum = 0
    for i in needed_numbers:
        sum += i
    return sum//len(needed_numbers)



if __name__ == '__main__':

    user_numbers = input("Enter numbers ").split(' ')
    # to int
    user_numbers_int = []
    for x in user_numbers:
        user_numbers_int.append(int(x))
    
    average_from_list(user_numbers_int)
    print(user_numbers)
    print(f'Average is {average_from_list(user_numbers_int)}')

"""
tests
"""
"""
    test1 = [1 ,2, 3, 4, 100]
    print(test1, "->", average_from_list(test1), )

    test2 = [1, 1, 5, 5, 10, 8, 7]
    print(test2, "->", average_from_list(test2), )

    test3 = [1000, 0, 1, 99]
    print(test3, "->", average_from_list(test3), )
"""