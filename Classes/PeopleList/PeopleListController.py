from Classes.PeopleList.PeopleList import PeopleList


class PeopleListController:
    def __init__(self):
        super(PeopleListController, self).__init__()
        self.model = PeopleList()

    def get_people_list(self):
        return self.model.get_people_list()

    def update_person_by_id(self, id_person, name, surname, mail, password, date_of_birth, place_of_birth, phone_number,
                            address, job):
        return self.model.update_person_by_id(id_person, name, surname, mail, password, date_of_birth, place_of_birth,
                                              phone_number, address, job)
