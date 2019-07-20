"""
Animals
"""

class Dog:



    def __init__(self, sex):
        self.age = 0
        self.sex = sex


    def setage(self, set_age):
        pass

    def getage(self):
        pass

    def showage(show_age):
        return show_age

    def speak(self):
        print('WOOF!')

    def set_sex(self):
        if self.sex == 'female dog':
            print('Suka')
        elif self.sex == 'male dog':
            print('Pies')


class Terier(Dog):
    age = 0
    breed = 'Terier'

class German_shepherd(Dog):
    breed = 'German shepherd'

class Bulldog(Dog):
    age = 0



if __name__ == '__main__':
    dog1 = Dog('male dog')
    dog1.speak()
    dog2 = Terier('female dog')
    dog2.breed
    


    print(dog1)
    print(f'{dog2.set_sex} to {dog2.breed} w wieku {dog2.age} lat')

