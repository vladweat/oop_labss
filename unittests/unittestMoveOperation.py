import unittest

from classes.MoveOperation import *


class TestMoveOperation(unittest.TestCase):
    def setUp(self):
        self.move_operation = MoveOperation()

    def test_move_test_set_new_location(self):
        self.move_operation.set_new_location('dep23')
        self.assertEqual(self.move_operation.new_location, 'dep23')

    def test_move_test_set_old_location(self):
        self.move_operation.set_old_location('main dep')
        self.assertEqual(self.move_operation.old_location, 'main dep')

    def test_move_test_set_tech(self):
        self.move_operation.set_tech('HP 345')
        self.assertEqual(self.move_operation.tech, 'HP 345')

    def test_move_test_set_date(self):
        self.move_operation.set_date('02.03.2021')
        self.assertEqual(self.move_operation.date, '02.03.2021')

if __name__ == '__main__':
    unittest.main()