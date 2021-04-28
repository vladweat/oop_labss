from classes.User import *


class MaterialRespOfDepartment(User):
    """Class HeadOfDepartment represents a user with a role Material Respondent Of Department"""

    def __init__(self, full_name=None):
        super().__init__()
        self.__full_name = full_name

        self.__call_num = 0

        self.split_full_name()

    @property
    def full_name(self):
        return self.__full_name

    @property
    def call_num(self):
        return self.__call_num

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

    def __call__(self):
        self.__call_num += 1

    def __str__(self):
        return f'Num of all calls of this object is {self.call_num}'


if __name__ == '__main__':
    mat_resp = MaterialRespOfDepartment(full_name='Kononov Vladislav Andreevich')
    mat_resp()
    mat_resp()
    mat_resp()
    mat_resp()
    mat_resp()
    print(mat_resp)
