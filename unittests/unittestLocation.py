import unittest

from classes.Location import *


class TestLocation(unittest.TestCase):

    def setUp(self):
        self.location = Location()

    def test_location_set_num_of_room(self):
        self.location.set_num_of_room(35)
        self.assertEqual(self.location.get_num_of_room(), 35)

    def test_location_set_department(self):
        self.location.set_department('dep3')
        self.assertEqual(self.location.department, 'dep3')

    def test_location_add_in_tech(self):
        for i in range(3):
            self.location.add_in_techs(i)
        self.assertEqual(self.location.techs, [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
