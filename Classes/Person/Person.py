class Person:
    def __init__(self, id_person, name, surname, mail, password, date_of_birth, place_of_birth, phone_number, address,
                 job):
        super(Person, self).__init__()
        self.id_person = id_person
        self.name = name
        self.surname = surname
        self.mail = mail
        self.password = password
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
        self.phone_number = phone_number
        self.address = address
        self.job = job
