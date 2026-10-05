class InsufficientFundsError(Exception):
    """Raised when a withdrawal is larger than the balance."""
    pass


class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Starting balance cannot be negative")
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self.transactions.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough money in the account")
        self.balance -= amount
        self.transactions.append(("withdraw", amount))

    def transfer_to(self, other_account, amount):
        self.withdraw(amount)          # raises an error if there isn't enough
        other_account.deposit(amount)

    def save_statement(self, filename):
        """Write one line per transaction to a text file."""
        with open(filename, "w") as file:
            file.write(f"Statement for {self.owner}\n")
            for kind, amount in self.transactions:
                file.write(f"{kind}: {amount}\n")
            file.write(f"balance: {self.balance}\n")
