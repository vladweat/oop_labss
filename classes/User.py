"""Module contains main class User and other things"""

import pickle

_next_id = 0


def _next_id_num():
    global _next_id
    _next_id += 1
    return _next_id


class User:
    """
    Class User.
    """
    def __init__(self, login=None, password=None, full_name=None, role=None):
        self._id = _next_id_num()
        self.__login = login
        self.__password = password
        self.__full_name = full_name
        self.role = role

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @property
    def full_name(self):
        return self.__full_name


    def get_login(self):
        return self.__login

    def set_login(self, login):
        self.__login = login

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_full_name(self):
        return self.__full_name

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def __str__(self):
        return f"User id: {self._id} login: {self.__login}, password: {self.__password}, full_name: {self.__full_name}, role: {self.role}"

    # def __del__(self):
    #     with open('D:\Python\oop_labs\dels\sys_user.txt', 'a', encoding='utf-8') as f:
    #         f.write(f'id {self._id}: name - {self.full_name}, role - {self.role}, {self.login}/{self.password}\n')
    #     f.close()


class PersistenceUser(object):
    @staticmethod
    def serialize(user):
        with open('user_dump', 'wb') as f:
            pickle.dump(user, f)
        f.close()

    @staticmethod
    def deserialize():
        with open('user_dump', 'rb') as f:
            user = pickle.load(f)
        f.close()
        return user


def test_user(user):
    entered_login = input(f"enter login of user: ")
    user.set_login(entered_login)

    entered_password = input(f"enter password of user: ")
    user.set_password(entered_password)

    entered_full_name = input(f"enter full name of user: ")
    user.set_full_name(entered_full_name)

    entered_role = input(f"enter role of user: ")
    user.set_role(entered_role)


if __name__ == '__main__':
    user = User(login='user1', password='123', full_name='Kononov V.A.', role='admin')

    PersistenceUser.serialize(user)

    user1 = PersistenceUser.deserialize()
    print(user1)
