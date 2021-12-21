class BusinessPartner:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        print("name:", self.name)


class Customer(BusinessPartner):
    def __init__(self, name, credit_limit):
        super().__init__(name)
        self.credit_limit = credit_limit

    def get_info(self):
        print("name:", self.name, ", credit limit:", self.credit_limit)


class Supplier(BusinessPartner):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
