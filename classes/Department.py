"""Module contains main class Department and other things"""
import pickle
from classes.HeadOfDepartment import *
from classes.MaterialRespOfDepartment import *
from classes.Exception import CheckingDate, Log, LogTime


_next_num_dep = 0


def _next_num_of_dep():
    global _next_num_dep
    _next_num_dep += 1
    return _next_num_dep


class Department:
    """
    Class Department.
    123ewq
    :param str short_name: short name of department
    :param str full_name: long/full name of department
    :param cls head_of_department: user with role HEAD
    :param cls resp_of_department: user with role MATERIALRESP
    :param list list_of_tech: list/array with all techs in current department
    :param list locations: list/array with all locations/rooms in current department

    """

    def __init__(self, short_name=None, full_name=None, head_of_department=None,
                 resp_of_department=None):
        super(Department, self).__init__()
        self._num_of_dep = _next_num_of_dep()
        self.short_name = short_name
        self.__full_name = full_name
        self.head_dep = head_of_department
        self.resp_dep = resp_of_department
        self.list_of_tech = []
        self.locations = []

    @property
    def full_name(self):
        return self.__full_name

    def get_num_of_dep(self):
        """:return int num_of_dep"""
        return self._num_of_dep

    @Log
    def set_num_of_dep(self, number_of_department):
        self._num_of_dep = number_of_department

    def get_short_name(self):
        """:return str short_name"""
        return self.short_name

    def set_short_name(self, short_name):
        self.short_name = short_name

    def get_full_name(self):
        """:return str full_name"""
        return self.__full_name

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def get_head_dep(self):
        """:return cls head_dep"""
        return self.head_dep

    @LogTime
    def set_head_dep(self, head_of_department):
        self.head_dep = head_of_department

    def get_resp_dep(self):
        """:return cls resp_dep"""
        return self.resp_dep

    def set_resp_dep(self, resp_of_department):
        self.resp_dep = resp_of_department

    def get_list_of_tech(self):
        """:return list list_of_tech"""
        return self.list_of_tech

    def add_in_list_of_tech(self, tech):
        self.list_of_tech.append(tech)

    def get_locations(self):
        """:return list locations"""
        return self.locations

    def add_in_locations(self, location):
        self.locations.append(location)


    def __str__(self):
        return f"Department num: {self._num_of_dep}, short name: {self.short_name}, " \
               f"full name: {self.__full_name}, head of dep: {self.head_dep}, " \
               f"resp of dep: {self.resp_dep}, techs: {self.list_of_tech}, rooms: {self.locations}"

    # def __del__(self):
    #     with open('D:\Python\oop_labs\dels\department.txt', 'a', encoding='utf-8') as f:
    #         f.write(f'department {self._num_of_dep}: name - {self.full_name} ({self.short_name}), '
    #                 f'stuff: head {self.head_dep}, material resp {self.resp_dep}, '
    #                 f'structure: techs - {self.list_of_tech}, locations - {self.locations}\n')
    #     f.close()


def test_department(department):
    """function for console create class Department"""
    num = input(f"enter inv number of tech: ")

    if num != '':
        department.set_num_of_dep(num)

    entered_short_name = input(f"enter short name of department №{department._num_of_dep}: ")
    department.set_short_name(entered_short_name)

    entered_full_name = input(f"enter full name of department №{department._num_of_dep}: ")
    department.set_full_name(entered_full_name)

    entered_head_dep = input(f"enter head of department №{department._num_of_dep}: ")
    department.set_head_dep(entered_head_dep)

    entered_resp_dep = input(f"enter material resp of department №{department._num_of_dep}: ")
    department.set_head_dep(entered_resp_dep)

    while True:
        answ = input("Want to add another tech (y/n): ")
        if answ.lower() == 'y':
            entered_tech = int(input("Write inv number of tech: "))
            department.add_in_list_of_tech(entered_tech)
        else:
            break

    while True:
        answ = input("Want to add another location (y/n): ")
        if answ.lower() == 'y':
            entered_location = int(input("Write num of room: "))
            department.add_in_locations(entered_location)
        else:
            break


class PersistenceDepartment(object):
    @staticmethod
    def serialize(department):
        with open('department_dump', 'wb') as f:
            pickle.dump(department, f)
        f.close()

    @staticmethod
    def deserialize():
        with open('department_dump', 'rb') as f:
            department = pickle.load(f)
        f.close()
        return department


def log(func):
    def wrapper(*args, **kwargs):
        print('call func {0}'.format(func.__name__), args, kwargs)
        func(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    head1 = HeadOfDepartment('Kononov Vladislav Andreevich')
    mat_resp1 = MaterialRespOfDepartment('Ivanov Ivan Ivanovich')
    dep1 = Department('DEP #1', 'Department #1', head1, mat_resp1)

    print(dep1)
