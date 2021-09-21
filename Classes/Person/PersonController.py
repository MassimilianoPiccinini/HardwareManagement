class PersonController:
    def __init__(self, person):
        self.model = person

    def get_id(self):
        return self.model.id_person

    def get_name(self):
        return self.model.name

    def get_surname(self):
        return self.model.surname

    def get_mail(self):
        return self.model.mail

    def get_password(self):
        return self.model.password

    def get_date_of_birth(self):
        return self.model.date_of_birth

    def get_place_of_birth(self):
        return self.model.place_of_birth

    def get_phone_number(self):
        return self.model.phone_number

    def get_address(self):
        return self.model.address

    def get_job(self):
        return self.model.job

    def set_id(self, id_person):
        self.model.id_person = id_person

    def set_name(self, name):
        self.model.name = name

    def set_surname(self, surname):
        self.model.surname = surname

    def set_mail(self, mail):
        self.model.mail = mail

    def set_password(self, password):
        self.model.password = password

    def set_date_of_birth(self, date_of_birth):
        self.model.date_of_birth = date_of_birth

    def set_place_of_birth(self, place_of_birth):
        self.model.place_of_birth = place_of_birth

    def set_phone_number(self, phone_number):
        self.model.phone_number = phone_number

    def set_address(self, address):
        self.model.address = address

    def set_job(self, job):
        self.model.job = job
