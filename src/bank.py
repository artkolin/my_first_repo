"""
Accounts
"""
import random

class Account:
    def __init__(self, number, first_name, last_name, balance=0):
        self._number = number
        self.first_name = first_name
        self.last_name = last_name
        self._balance = balance


    @property
    def owner(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    def transfer(self, ammount):
        self._balance +=ammount





class Card:
    def __init__(self, account, ):
        self._account = account
        self._pin = random.sample(range(10), 5)

    def __str__(self):
        return f'Card({self._account.owner})'

    def check_pin(self):
        return pin == self._pin

    def get_account(self):
        return self._account