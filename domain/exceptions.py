class TransactionException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message


class DuplicatedEmailException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message