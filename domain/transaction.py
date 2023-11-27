from datetime import datetime
from domain.utils import time_as_string


class Transaction():
    def __init__(self, amount, transaction_type):
        self.created_at = datetime.now()
        self.transaction_type = transaction_type
        self.amount = amount

    def __str__(self):
        return "%20s - %10s - %7s" % (time_as_string(self.created_at), self.transaction_type, self.amount)
