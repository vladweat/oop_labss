import unittest

from classes.Department import *


class TestDepartment(unittest.TestCase):

    def setUp(self):
        self.department = Department()

    def test_department_set_num_of_dep(self):
        self.department.set_num_of_dep(34)
        self.assertEqual(self.department.get_num_of_dep(), 34)

    def test_department_set_short_name(self):
        self.department.set_short_name('dep1')
        self.assertEqual(self.department.short_name, 'dep1')

    def test_department_set_full_name(self):
        self.department.set_full_name('department 1')
        self.assertEqual(self.department.full_name, 'department 1')

    def test_department_set_head_of_dep(self):
        self.department.set_head_dep('head 1')
        self.assertEqual(self.department.head_dep, 'head 1')

    def test_department_set_resp_of_dep(self):
        self.department.set_resp_dep('resp 1')
        self.assertEqual(self.department.resp_dep, 'resp 1')

    def test_department_add_in_list_of_tech(self):
        for i in range(3):
            self.department.add_in_list_of_tech(i)
        self.assertEqual(self.department.list_of_tech, [0, 1, 2])

    def test_department_add_in_locations(self):
        for i in range(3):
            self.department.add_in_locations(i)
        self.assertEqual(self.department.locations, [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
