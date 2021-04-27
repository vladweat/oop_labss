import unittest

from classes.User import *


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User(login='login1', password='pass1', full_name='Test T.T.', role='test')

    def test_user_set_login(self):
        self.user.set_login('KononovV')
        self.assertEqual(self.user.login, 'KononovV')

    def test_user_set_password(self):
        self.user.set_password('123qweR')
        self.assertEqual(self.user.password, '123qweR')

    def test_user_set_full_name(self):
        self.user.set_full_name('Kononov V.A.')
        self.assertEqual(self.user.full_name, 'Kononov V.A.')

    def test_user_set_role(self):
        self.user.set_role('admin')
        self.assertEqual(self.user.role, 'admin')


if __name__ == '__main__':
    unittest.main()
