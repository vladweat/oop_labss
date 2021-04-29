from classes.User import *


class MaterialRespOfDepartment(User):
    """Class HeadOfDepartment represents a user with a role Material Respondent Of Department"""

    def __init__(self, full_name=None):
        super().__init__()
        self.__full_name = full_name
        self.role = 'Material Resp of Department'
        self.__call_num = 0

        self.split_full_name(self.__full_name)

    @property
    def full_name(self):
        return self.__full_name

    @property
    def call_num(self):
        return self.__call_num

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

    def __call__(self):
        self.__call_num += 1

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


# if __name__ == '__main__':
#     mat_resp = MaterialRespOfDepartment(full_name='Kononov Vladislav Andreevich')
#     print(mat_resp.get_role())