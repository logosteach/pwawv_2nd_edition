import os
import unittest
from bank_account import BankAccount, InsufficientFundsError


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Runs before EVERY test, so each test gets a brand-new account.
        self.account = BankAccount("Ada", 100)

    # ---------- Testing the starting state ----------
    def test_new_account_has_owner(self):
        self.assertEqual(self.account.owner, "Ada")

    def test_new_account_has_starting_balance(self):
        self.assertEqual(self.account.balance, 100)

    def test_new_account_has_no_transactions(self):
        self.assertEqual(self.account.transactions, [])

    def test_default_balance_is_zero(self):
        empty = BankAccount("Grace")
        self.assertEqual(empty.balance, 0)

    def test_negative_starting_balance_raises(self):
        with self.assertRaises(ValueError):
            BankAccount("Bad", -5)

    # ---------- Testing methods that change state ----------
    def test_deposit_increases_balance(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_is_recorded(self):
        self.account.deposit(50)
        self.assertEqual(self.account.transactions, [("deposit", 50)])

    def test_withdraw_decreases_balance(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

    def test_withdraw_entire_balance(self):
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 0)

    # ---------- Testing errors ----------
    def test_deposit_zero_raises(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_overdraw_raises(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(500)

    def test_failed_withdraw_leaves_balance_unchanged(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(500)
        self.assertEqual(self.account.balance, 100)

    # ---------- Testing two objects together ----------
    def test_transfer_moves_money(self):
        friend = BankAccount("Grace", 10)
        self.account.transfer_to(friend, 40)
        self.assertEqual(self.account.balance, 60)
        self.assertEqual(friend.balance, 50)


class TestStatementFile(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Ada", 100)
        self.filename = "test_statement.txt"

    def tearDown(self):
        # Runs after EVERY test, even if the test failed.
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_statement_lists_transactions(self):
        self.account.deposit(25)
        self.account.save_statement(self.filename)
        with open(self.filename) as file:
            contents = file.read()
        self.assertIn("deposit: 25", contents)
        self.assertIn("balance: 125", contents)


if __name__ == "__main__":
    unittest.main()
