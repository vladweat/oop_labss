"""Module contains main class HeadOfDepartment and other things"""
from classes.User import *
from classes.Department import *


class HeadOfDepartment(User):
    """Class HeadOfDepartment represents a user with a role Head Of Department"""

    def __init__(self, full_name=None):
        super().__init__()
        self.__full_name = full_name
        self.role = 'Head of Department'

        self.split_full_name(self.__full_name)

    @property
    def full_name(self):
        return self.__full_name

    def split_full_name(self, name_to_split):

        fio = str(name_to_split).split(' ')
        self.name = fio[0]
        self.surname = fio[1]
        self.patronymic = fio[2]

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_patronymic(self):
        return self.patronymic

    def __call__(self, new_full_name):
        self.split_full_name(new_full_name)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


# if __name__ == '__main__':
#     head = HeadOfDepartment(full_name='Kononov Vladislav Andreevich')
#     dep1 = Department(short_name='first dep', head_of_department=head)
#     # #
#     # # print(head.name)
#     #
#     # print(head.role)
#     # print(head)
#     # print(f'Dep {dep1.get_short_name()}, head {dep1.head_dep.name} {dep1.head_dep.surname}\n\n')
#     # print(dep1.head_dep.full_name)
#     # print(head.full_name)
#     # print(head.name)
#     print(head)
#     head('Ivanov Ivan Ivanovich')
#     print(head)
#     print(HeadOfDepartment.__doc__)


