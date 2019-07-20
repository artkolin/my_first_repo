def fibonacci(user_number):
    if user_number == 0:
        return 0
    elif user_number == 1:
        return 1
    else:
        return fibonacci(user_number -1) + fibonacci(user_number -2)

if __name__ == '__main__':
    user_input = int(input("How many Fibonacci number do you want: "))
    for i in range(user_input):
        print(fibonacci(i))