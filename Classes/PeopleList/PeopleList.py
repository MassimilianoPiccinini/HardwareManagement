import json

from Classes.Person.Person import Person


def is_person_in_database(id_person):
    with open("Classes/Person/users.txt", 'r') as f:
        for person in json.load(f):
            if person['id'] == id_person:
                return True
        f.close()
        return False


class PeopleList:

    def __init__(self):
        super(PeopleList, self).__init__()
        self.people_list = self.get_people_list()

    def get_people_list(self):
        people_array = []
        with open("Classes/Person/users.txt", 'r') as f:
            for person in json.load(f):
                my_person = Person(person["id"],
                                   person["name"],
                                   person["surname"],
                                   person["mail"],
                                   person["password"],
                                   person["date_of_birth"],
                                   person["place_of_birth"],
                                   person["phone_number"],
                                   person["address"],
                                   person["job"])
                people_array.append(my_person)
        return people_array

    def update_person_by_id(self, id_person, name, surname, mail, password, date_of_birth, place_of_birth,
                            phone_number, address, job):
        if is_person_in_database(id_person):
            with open("Classes/Person/users.txt", 'r') as f:
                people_array = json.load(f)
                for person in people_array:
                    if person['id'] == id_person:
                        person['name'] = name
                        person['surname'] = surname
                        person['mail'] = mail
                        person['password'] = password
                        person['date_of_birth'] = date_of_birth
                        person['place_of_birth'] = place_of_birth
                        person['phone_number'] = phone_number
                        person['address'] = address
                        person['job'] = job
                        my_person = Person(id_person, name, surname, mail, password, date_of_birth, place_of_birth,
                                           phone_number, address, job)
                        index = 0
                        for pers in people_array:
                            if pers['id'] == id_person:
                                break
                            index = index + 1

                        people_array[index] = {
                            'id': id_person,
                            'name': name,
                            'surname': surname,
                            'mail': mail,
                            'password': password,
                            'date_of_birth': date_of_birth,
                            'place_of_birth': place_of_birth,
                            'phone_number': phone_number,
                            'address': address,
                            'job': job
                        }
                        self.people_list[index] = my_person
                        break

                j = json.dumps(people_array)
                with open("Classes/Person/users.txt", 'w') as fw:
                    fw.write(j)
                    fw.close()
            f.close()
            return True
        return False
