from classes.User import *


class MaterialRespOfDepartment(User):
    """Class HeadOfDepartment represents a user with a role Material Respondent Of Department"""

    def __init__(self, full_name=None):
        super().__init__()
        self.__full_name = full_name

        self.split_full_name()

    @property
    def full_name(self):
        return self.__full_name

    def split_full_name(self):
        fio = str(self.__full_name).split(' ')
        self.name = fio[0]
        self.surname = fio[1]
        self.patronymic = fio[2]

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_patronymic(self):
        return self.patronymic
