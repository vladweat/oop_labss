"""Module contains main class Location and other things"""
import pickle

_next_room = 0


def _next_num_of_room():
    global _next_room
    _next_room += 1
    return _next_room


class Location:
    """
    Class Department.
    """
    def __init__(self, department=None):
        self._num_of_room = _next_num_of_room()
        self.techs = []
        self.department = department

    def get_num_of_room(self):
        return self._num_of_room

    def set_num_of_room(self, num_of_room):
        self._num_of_room = num_of_room

    def get_techs(self):
        return self.techs

    def add_in_techs(self, tech):
        self.techs.append(tech)

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department

    def __str__(self):
        return f"Location num of room: {self._num_of_room}, department #: {self.department._num_of_dep}, techs: {self.techs}"

    # def __del__(self):
    #     path = 'D:\Python\oop_labs\dels\location.txt'
    #     with open(path, 'a', encoding='utf-8') as f:
    #         f.write(f'room {self._num_of_room}: department - {self.department}, techs - {self.techs}\n')
    #     f.close()


def test_location(location):
    num = input(f"enter number of room: ")

    if num != '':
        location.set_num_of_room(num_of_room=num)

    entered_department = input(f"enter department of room {location._num_of_room}: ")
    location.set_department(entered_department)

    while True:
        answ = input("Want to add another tech (y/n): ")
        if answ.lower() == 'y':
            entered_tech = int(input("Write inv number of tech: "))
            location.add_in_techs(entered_tech)
        if answ.lower() == 'n':
            break


class PersistenceMoveOperation(object):
    @staticmethod
    def serialize(location):
        with open('location_dump', 'wb') as f:
            pickle.dump(location, f)
        f.close()

    @staticmethod
    def deserialize():
        with open('location_dump', 'rb') as f:
            location = pickle.load(f)
        f.close()
        return location
