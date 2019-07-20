import unittest
from src.bank import Account, Card
class AccountTestCase(unittest.TestCase):

    def test_account(self):
        new_acc = Account(12345677, 'Jan', 'Kowalski', 5000)
        new_acc2 = Account(4563666, 'Pawel', 'Jakistam', )
        self.assertEqual(new_acc.number, 12345677)
        self.assertEqual(new_acc.owner, 'Jan Kowalski')
        self.assertEqual(new_acc.balance, 5000)



    def test_transfer(self):
        pass