"""Module contains main class Tech and other things"""


import pickle
from classes.Exception import CheckingDate, CheckingPrice

_next_inv_num = 0


def _next_inv_number():
    global _next_inv_num
    _next_inv_num += 1
    return _next_inv_num


class Tech:
    """
    Class Tech.
    """
    def __init__(self, name=None, model=None, date_of_purchase=None, price=None,
                 current_location=None):
        self._inventory_number = _next_inv_number()
        self.name = name
        self.model = model
        self.date_of_purchase = CheckingDate()
        self.price = CheckingPrice()
        self.current_location = current_location

    def get_inventory_number(self):
        return self._inventory_number

    def set_inventory_number(self, inventory_number):
        self._inventory_number = inventory_number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_date_of_purchase(self):
        return self.date_of_purchase

    def set_date_of_purchase(self, date_of_purchase):
        self.date_of_purchase = date_of_purchase

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_current_location(self):
        return self.current_location

    def set_current_location(self, current_location):
        self.current_location = current_location

    def __str__(self):
        return f"Tech inv number: {self._inventory_number}, name: {self.name}, model: {self.model}, " \
               f"purchase date: {self.date_of_purchase}, price: {self.price}, location: {self.current_location}"

    def __del__(self):
        with open('D:\Python\oop_labs\dels/tech.txt', 'a', encoding='utf-8') as f:
            f.write(f'tech {self._inventory_number}: name - {self.name}, model - {self.model}, price - {self.price}, '
                    f'date of purchase - {self.date_of_purchase}, current location - {self.current_location}\n')
        f.close()

class PersistenceTech(object):
    @staticmethod
    def serialize(tech):
        with open('tech_dump', 'wb') as f:
            pickle.dump(tech, f)
        f.close()

    @staticmethod
    def deserialize():
        with open('tech_dump', 'rb') as f:
            tech = pickle.load(f)
        f.close()
        return tech


def test_tech(tech):
    num = input(f"enter inv number of tech: ")

    if num != '':
        tech.set_inventory_number(num)

    entered_name = input(f"enter name of tech №{tech._inventory_number}: ")
    tech.set_name(entered_name)

    entered_model = input(f"enter model of tech №{tech._inventory_number}: ")
    tech.set_model(entered_model)

    entered_date = input(f"enter date of perchase of tech №{tech._inventory_number}: ")
    tech.set_date_of_purchase(entered_date)

    entered_price = input(f"enter price of tech №{tech._inventory_number}: ")
    tech.set_price(entered_price)

    entered_location = input(f"enter current location of tech №{tech._inventory_number}: ")
    tech.set_current_location(entered_location)
