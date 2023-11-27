from domain.customer import Customer
from domain.account import Account
from domain.transaction import Transaction
from domain.exceptions import TransactionException, DuplicatedEmailException

from usecases.account_service import acc_srv
from usecases.transaction_service import tx_srv


if __name__ == '__main__':
    # Create an account for a customer who does not exist in the system; the customer will be created along with the account.
    acc: Account = acc_srv.create_account(None, "Duong", "duongpv@outlook.com", "0977123123")
    tx_srv.make_transaction(acc.account_id, "deposit", 3000)
    tx_srv.make_transaction(acc.account_id, "withdraw", 400)
    tx_srv.make_transaction(acc.account_id, "deposit", 50)

    tx_srv.generate_account_statement(acc.account_id)

    # Check the current balance
    assert (acc.get_balance() == 2650)

    customer: Customer = acc_srv.get_customer_by_id(acc.customer_id)
    assert customer.phone_number == "0977123123"

    # Create another account for same customer, update the phone number
    customer_id = acc.customer_id
    acc_srv.create_account(customer_id, "", "", "0988111222")

    customer: Customer = acc_srv.get_customer_by_id(acc.customer_id)

    # Customer phone number updated
    assert customer.phone_number == "0988111222"

    accounts = acc_srv.get_accounts_by_customer_id(customer.customer_id)
    # This customer now has 2 accounts
    assert len(accounts) == 2

    try:
        customer: Customer = acc_srv.create_customer("FakeName", "duongpv@outlook.com", "0901222900")
    except DuplicatedEmailException as e:
        print ("Email already existed. Cannot create new customer")
        # This will result in an exception since the customer's email is already registered
        assert e.code == 1001

    # Create another customer
    customer: Customer = acc_srv.create_customer("Bill", "bill@gmail.com", "0901222900")
    acc: Account = acc_srv.create_account(customer.customer_id, None, None, None)

    try:
        tx_srv.make_transaction(acc.account_id, "withdraw", 400)
    except TransactionException as e:
        # This will result in an exception since the newly created account does not have enough funds
        assert e.code == 1002

    tx_srv.make_transaction(acc.account_id, "deposit", 1000)
    tx_srv.make_transaction(acc.account_id, "withdraw", 400)
    assert (acc.get_balance() == 600)

    tx_srv.generate_account_statement(acc.account_id)
