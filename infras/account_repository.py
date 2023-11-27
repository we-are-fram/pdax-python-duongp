from domain.customer import Customer
from domain.account import Account
from domain.exceptions import DuplicatedEmailException
from domain.utils import generate_sequence_id


class AccountRepository():
    def __init__(self):
        # For testing purposes, just use simple in-memory storage
        self.customers = {}
        self.accounts = {}
    
    def save_customer(self, customer: Customer) -> Customer:
        if not customer.email:
            raise Exception("Cannot create a customer without email")
        
        # This should be handled by a database constraint, as the email should be unique
        for c in self.customers.values():
            if c.email == customer.email:
                raise DuplicatedEmailException(1001, "This email already registered")

        # Don't need this utils function when we use a database that natively supports sequence ID generation.
        customer_id = generate_sequence_id("customer")

        customer.customer_id = customer_id
        self.customers[customer_id] = customer

        return self.customers[customer_id]

    def get_customer_by_id(self, customer_id):
        return self.customers.get(customer_id)

    def update_customer(self, customer_id, data: dict):
        customer: Customer = self.get_customer_by_id(customer_id)
        if not customer:
            raise Exception("The customer does not exist in the system")

        customer.update(data)
        self.customers[customer_id] = customer

        return self.customers[customer_id]

    def save_account(self, account: Account) -> Account:
        customer: Customer = self.get_customer_by_id(account.customer_id)
        if not customer:
            raise Exception("The customer does not exist in the system")

        # Don't need this utils function when we use a database that natively supports sequence ID generation.
        account.account_id = generate_sequence_id("account")
        account.account_number = account.generate_account_number(account.account_id)

        self.accounts[account.account_id] = account

        return self.accounts[account.account_id]

    def find_account_by_id(self, account_id) -> Account:
        return self.accounts.get(account_id)

    def find_accounts_by_customer_id(self, customer_id) -> list:
        return [account for account in self.accounts.values() if account.customer_id == customer_id]


repository = AccountRepository()
