"""
Employee classes
"""
import datetime


class Employee:
    """Represents an employee"""
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@example.com'


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print('deleted')


    @classmethod
    def set_raise_ammount(cls, new_raise_amount):
        cls.raise_amount = new_raise_amount


    @staticmethod
    def is_workday(day):
        return day.weekday() not in (5, 6)


if __name__ == '__main__':

    emp = Employee('Jan', 'Kowalski', 2000)
    emp.fullname = 'Jan Nowak'
    print(emp.fullname)
    del emp.fullname
    print(emp.fullname)



    """
    today = datetime.date.today()
    day = today + datetime.timedelta(1)
    print('Is workday? ', Employee.is_workday(day))
    """


    """
    print(Employee.raise_amount)
    old_emp = Employee('Stefan', 'Wąs', 2000)
    old_emp.apply_raise()
    print(old_emp.fullname(), old_emp.pay)

    Employee.raise_amount = 1.1
    print(Employee.raise_amount)
    new_emp = Employee('Tadeusz', 'Kowalski', 2000)
    new_emp.apply_raise()
    print(new_emp.fullname(), new_emp.pay)
    

    print(Employee.raise_amount)
    Employee.set_raise_ammount(1.1)
    print(Employee.raise_amount)
    """

