from infras.account_repository import Account, Customer, repository as account_repository


class AccountService():
    def create_customer(self, name, email, phone_number) -> Customer:
        customer = Customer({
            'name': name,
            'email': email,
            'phone_number': phone_number
        })

        return account_repository.save_customer(customer)

    def get_customer_by_id(self, customer_id) -> Customer:
        return account_repository.get_customer_by_id(customer_id)

    def create_account(self, customer_id, name, email, phone_number) -> Account:
        if not customer_id:
            customer: Customer = self.create_customer(name, email, phone_number)

        else:
            customer: Customer = account_repository.update_customer(
                customer_id=customer_id, 
                data={
                    'name': name,
                    'email': email,
                    'phone_number': phone_number
                }
            )

        account: Account = Account({
            'customer_id': customer.customer_id
        })
        
        account = account_repository.save_account(account)

        print ("[{}] New account created: {}".format(customer.email, account.account_number))
        return account

    def get_accounts_by_customer_id(self, customer_id) -> list:
        return account_repository.find_accounts_by_customer_id(customer_id)


acc_srv = AccountService()