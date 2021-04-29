"""Module contains main class MoveOperation and other things"""
import datetime
import pickle

from classes.Exception import CheckingDate, Log, LogTime
from classes.Location import *
from classes.Tech import *


class MoveOperation(Location, Tech):
    """
    Class MoveOperation.
    """

    def __init__(self, new_location=None, old_location=None, tech=None, date=None):
        super(MoveOperation, self).__init__()
        self.new_location = Location(department=new_location)
        self.old_location = old_location
        self.tech = tech
        self.date = CheckingDate()

    def get_new_location(self):
        return self.new_location

    def set_new_location(self, new_location):
        self.new_location = new_location

    def get_old_location(self):
        return self.old_location

    def set_old_location(self, old_location):
        self.old_location = old_location

    def get_tech(self):
        return self.tech

    def set_tech(self, tech):
        self.tech = tech

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def __str__(self):
        return f"Move info: old location: {self.old_location.get_department()}, new location: {self.new_location.get_department()}, " \
               f"tech №: {self.tech.get_inventory_number()}, date: {self.date}"

    # def __del__(self):
    #     with open('D:\Python\oop_labs\dels\move_operation.txt', 'a', encoding='utf-8') as f:
    #         f.write(f'new location: {self.new_location}, old location: {self.old_location}, tech: {self.tech}, '
    #                 f'date: {self.date}\n')
    #     f.close()


class PersistenceMoveOperation(object):
    @staticmethod
    def serialize(move):
        with open('move_dump', 'wb') as f:
            pickle.dump(move, f)
        f.close()

    @staticmethod
    def deserialize():
        with open('move_dump', 'rb') as f:
            move = pickle.load(f)
        f.close()
        return move


def test_move_operation(move):
    entered_new_location = input(f"enter new location: ")
    move.set_new_location(entered_new_location)

    entered_old_location = input(f"enter old location: ")
    move.set_old_location(entered_old_location)

    entered_tech = input(f"enter inv number of tech: ")
    move.set_tech(entered_tech)

    entered_date = input(f"enter date: ")
    move.set_date(entered_date)


if __name__ == '__main__':
    tech1 = Tech('tech #1', 'model v2', (23, 10, 2000), 2000, 'dep56')
    mo1 = MoveOperation('dep1', tech1.current_location, tech1, date=datetime.date.today())

    print(tech1)
    print(mo1)
