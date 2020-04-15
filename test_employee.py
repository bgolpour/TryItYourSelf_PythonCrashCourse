import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.jon = Employee('Jon', 'Bonjovi', 65000)

    def test_give_default_raise(self):
        self.jon.give_raise()
        self.assertEqual(self.jon.salary,70000)

    def test_give_custom_raise(self):
        self.jon.give_raise(10000)
        self.assertEqual(self.jon.salary, 75000)
unittest.main()