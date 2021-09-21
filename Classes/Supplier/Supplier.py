class Supplier:
    def __init__(self, id_supplier, name, description, mail, phone_number, address):
        super(Supplier, self).__init__()
        self.id_supplier = id_supplier
        self.name = name
        self.description = description
        self.mail = mail
        self.phone_number = phone_number
        self.address = address
