"""
While loop
"""

def count_down(number):
    while number:
        print(number)
        number -= 1
    print('Lift off!')
"""
Basic while loop
"""

def premature_lift_off(number):
    while number:
        print(number)
        number -= 1
        if number == 5:
            break
    print('Lift off')

"""
Break while loop
"""

def even_count_down(number):
    while number:
        number -= 1
        if number % 2:
            continue
        print((number))

"""
Continue while loop
"""

if __name__ == '__main__':
    #count_down(10)
    even_count_down(10)