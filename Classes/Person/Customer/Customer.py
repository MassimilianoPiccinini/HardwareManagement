from Classes.Person.Person import Person


class Customer(Person):
    def __init__(self, id_person, name, surname, mail, password, date_of_birth, place_of_birth, phone_number, address,
                 job, payment_method, credit_card_number, permissions, valid_through, ccv, iban):
        super().__init__(id_person, name, surname, mail, password, date_of_birth, place_of_birth, phone_number, address,
                         job)
        self.payment_method = payment_method
        self.credit_card_number = credit_card_number
        self.permissions = permissions
        self.valid_through = valid_through
        self.ccv = ccv
        self.iban = iban
