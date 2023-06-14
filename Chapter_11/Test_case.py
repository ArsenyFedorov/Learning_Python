import unittest
from Task_1 import cite


class NameTest(unittest.TestCase):
    def test_firs_city(self):
        first_city = cite("Россия", "Москва")
        self.assertEqual(first_city, "Россия Москва")


    def test_people_cite(self):
        people_cite = cite("Россия", "Москва", 22222)
        self.assertEqual(people_cite, "Россия Москва -> People 22222")


if __name__ == "__main__":
    unittest.main()
