import my_module

if __name__ =='__main__':

    some_list = ['A', 1, 15, [1], ]
    a = 15
    print(
        f'Index of element {a}: ',
        my_module.find_index(some_list, a)
    )
    b = 100
    print(
        f'Index of element {b}: ',
        my_module.find_index(some_list, b)
    )