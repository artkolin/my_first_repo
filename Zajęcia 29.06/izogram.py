"""
Izogram jest słowem w którym żadna litera nie powtarza się.
Program ma po podaniu słowa stwierdzić czy słowo jest izogramem czy nie.
"""

def is_izogram(word):
    word = word.lower()
    letters = []
    for letter in word:
        if letter in letters:
            return False
        letters.append(letter)
    return True


def is_izogram_v2(word):
    return len(word) == len(set(word))


if __name__ == '__main__':
    user_word = input('Provide word: ')
    if is_izogram_v2(user_word):
        print('Izogram')
    else:
        print('Not izogram')