import time

from random import randint
from domain.transaction import Transaction
from domain.exceptions import TransactionException


REQUIRED_FIELD = [
    'customer_id'
]

class Account():
    @staticmethod
    def generate_account_number(account_id):
        # Random account number with 12 digits 
        return "{}{}".format(str(account_id).zfill(8), str(randint(1, 9999)).zfill(4))

    def __init__(self, data: dict):
        for field in REQUIRED_FIELD:
            if field not in data:
                raise Exception('Missing required field: {}'.format(field))

        self.customer_id = data['customer_id']
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        # Assume that we only allow depositing an integer amount
        if not str(amount).isnumeric():
            raise Exception("Amount should be a number")

        self.balance += int(amount)

        # Insertion into the database should be performed here
        self.transactions.append(Transaction(amount, "deposit"))

        # Just for testing
        time.sleep(1.0)

    def withdraw(self, amount):
        # Assume that we only allow withdrawing an integer amount
        if not str(amount).isnumeric():
            raise Exception("Amount should be a number")

        if self.balance < amount:
            raise TransactionException(1002, "Not enough balance")

        self.balance -= int(amount)

        # Insertion into the database should be performed here
        self.transactions.append(Transaction(amount, "withdraw"))

        # Just for testing
        time.sleep(1.0)

    def get_balance(self):
        return self.balance
