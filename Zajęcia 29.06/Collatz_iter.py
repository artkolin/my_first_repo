"""
Collatz algoritm solution
"""

def collatz(x):
    """Iterative version"""
    while True:
        print(x)
        if x == 1:
            break
        elif x % 2 != 0:
            x = x * 3 + 1
        else:
            x = x // 2

if __name__ == '__main__':
    number = int(input("Provide number: "))
    collatz(number)
