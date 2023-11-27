import json

from random import randint
from domain.utils import generate_sequence_id


REQUIRED_FIELD = [
    'name',
    'email'
]

class Customer():
    def __init__(self, data: dict):
        for field in REQUIRED_FIELD:
            if field not in data:
                raise Exception('Missing required field: {}'.format(field))

        for k in ['name', 'email', 'phone_number']:
            setattr(self, k, data.get(k))
    
    def update(self, data: dict):
        for k in ['name', 'email', 'phone_number']:
            if data.get(k):
                setattr(self, k, data[k])

    def __str__(self):
        return " Name:  %s \n Email: %s \n Phone: %s" % (self.name, self.email, self.phone_number)
