class SupplierController:
    def __init__(self, supplier):
        self.model = supplier

    def get_id_supplier(self):
        return self.model.id_supplier

    def set_id_supplier(self, id_supplier):
        self.model.id_supplier = id_supplier

    def get_name(self):
        return self.model.name

    def set_name(self, name):
        self.model.name = name

    def get_description(self):
        return self.model.description

    def set_description(self, description):
        self.model.description = description

    def get_mail(self):
        return self.model.mail

    def set_mail(self, mail):
        self.model.mail = mail

    def get_phone_number(self):
        return self.model.phone_number

    def set_phone_number(self, phone_number):
        self.model.phone_number = phone_number

    def get_address(self):
        return self.model.address

    def set_address(self, address):
        self.model.address = address

