import pytest
from bank_account import BankAccount, InsufficientFundsError


@pytest.fixture
def account():
    """A fresh account for each test (like setUp in unittest)."""
    return BankAccount("Ada", 100)


def test_starting_balance(account):
    assert account.balance == 100


def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150


def test_deposit_is_recorded(account):
    account.deposit(50)
    assert account.transactions == [("deposit", 50)]


def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70


def test_overdraw_raises(account):
    with pytest.raises(InsufficientFundsError):
        account.withdraw(500)


def test_transfer(account):
    friend = BankAccount("Grace", 10)
    account.transfer_to(friend, 40)
    assert account.balance == 60
    assert friend.balance == 50
