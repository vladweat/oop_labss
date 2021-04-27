import unittest

from classes.Tech import *


class TestTech(unittest.TestCase):

    def setUp(self):
        self.tech = Tech()

    def test_tech_set_inventory_num(self):
        self.tech.set_inventory_number(123)
        self.assertEqual(self.tech.get_inventory_number(), 123)

    def test_tech_set_name(self):
        self.tech.set_name('printer')
        self.assertEqual(self.tech.name, 'printer')

    def test_tech_set_model(self):
        self.tech.set_model('v2')
        self.assertEqual(self.tech.model, 'v2')

    def test_tech_set_date_of_purchase(self):
        self.tech.set_date_of_purchase('01.01.2020')
        self.assertEqual(self.tech.date_of_purchase, '01.01.2020')

    def test_tech_set_price(self):
        self.tech.set_price(1000)
        self.assertEqual(self.tech.price, 1000)

    def test_tech_set_current_location(self):
        self.tech.set_current_location('dep1')
        self.assertEqual(self.tech.current_location, 'dep1')


if __name__ == '__main__':
    unittest.main()
