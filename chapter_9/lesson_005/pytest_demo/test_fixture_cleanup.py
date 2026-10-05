import os
import pytest
from bank_account import BankAccount


@pytest.fixture
def statement_file():
    filename = "test_statement.txt"
    yield filename                 # the test runs here
    if os.path.exists(filename):   # cleanup code (like tearDown)
        os.remove(filename)


def test_statement_has_balance(statement_file):
    account = BankAccount("Ada", 100)
    account.save_statement(statement_file)
    with open(statement_file) as file:
        assert "balance: 100" in file.read()
