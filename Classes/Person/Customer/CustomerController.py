from Classes.Person.PersonController import PersonController


class CustomerController(PersonController):
    def __init__(self, customer):
        PersonController.__init__(self, customer)
        self.model = customer

    def get_payment_method(self):
        return self.model.payment_method

    def set_payment_method(self, payment_method):
        self.model.payment_method = payment_method

    def get_credit_card_number(self):
        return self.model.credit_card_number

    def set_credit_card_number(self, credit_card_number):
        self.model.credit_card_number = credit_card_number

    def get_valid_through(self):
        return self.model.valid_through

    def set_valid_through(self, valid_through):
        self.model.valid_through = valid_through

    def get_ccv(self):
        return self.model.ccv

    def set_ccv(self, ccv):
        self.model.ccv = ccv

    def get_iban(self):
        return self.model.iban

    def set_iban(self, iban):
        self.model.iban = iban
