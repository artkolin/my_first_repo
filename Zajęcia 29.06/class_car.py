"""
OOP example
"""

class Car:
    acceleration = 10

    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.in_motion = False
        self.speed = 0

    def drive(self):
        self.in_motion = True

    def accelerate(self):
        self.speed += self.acceleration

    def stop(self):
        self.in_motion = False
        self.speed = 0

    def print_reg_number_and_speed(self):
        print(f'')

if __name__ == "__main__":
    opel_astra = Car('EL012334')
    opel_astra.accelerate()
    opel_astra.print_reg_number_and_speed()
