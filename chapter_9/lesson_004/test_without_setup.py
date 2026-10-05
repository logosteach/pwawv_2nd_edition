import unittest
from bank_account import BankAccount


class TestRepetitive(unittest.TestCase):

    def test_deposit(self):
        account = BankAccount("Ada", 100)      # same line...
        account.deposit(50)
        self.assertEqual(account.balance, 150)

    def test_withdraw(self):
        account = BankAccount("Ada", 100)      # ...repeated...
        account.withdraw(30)
        self.assertEqual(account.balance, 70)

    def test_owner(self):
        account = BankAccount("Ada", 100)      # ...in every test!
        self.assertEqual(account.owner, "Ada")


if __name__ == "__main__":
    unittest.main()
