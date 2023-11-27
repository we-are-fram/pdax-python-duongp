from infras.account_repository import Account, Customer, repository as account_repository


class TransactionService():
    def make_transaction(self, account_id, transaction_type, amount):
        if transaction_type not in ["deposit", "withdraw"]:
            raise Exception("Unknown transaction type: {}".format(transaction_type))

        account: Account = account_repository.find_account_by_id(account_id)
        if not account:
            raise Exception("Account {} not found".format(account_id))

        getattr(account, transaction_type)(amount)

    def generate_account_statement(self, account_id) -> str:
        account: Account = account_repository.find_account_by_id(account_id)
        if not account:
            raise Exception("Account {} not found".format(account_id))

        statement = "Account info: \n"
        customer: Customer = account_repository.get_customer_by_id(account.customer_id)
        statement += str(customer)

        statement += "\nTransactions details: \n".format(account.account_number)
        for tx in account.transactions:
            statement += str(tx)
            statement += "\n"

        statement += "---------------------- \nCurrent balance: %7s" % account.balance

        print (statement)
        return statement


tx_srv = TransactionService()
