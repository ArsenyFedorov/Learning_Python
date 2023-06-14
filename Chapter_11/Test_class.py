from Task_2 import Employee
import unittest

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.fil = Employee("Fill", "Lyser", 1000)

    def test_one(self):
        self.salary_fil = self.fil.give_raise()
        self.assertEqual(self.salary_fil, 6000)

    def test_two(self):
        self.append_fil = self.fil.give_raise(1_000)
        self.assertEqual(self.append_fil, 2000)


if __name__ == "__main__":
    unittest.main()
