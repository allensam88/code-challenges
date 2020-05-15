import unittest
from duplicates import duplicates


class DuplicateTests(unittest.TestCase):
    def setUp(self):
        self.list1 = [1, 2, 3, 1]
        self.list2 = [1, 2, 3, 4]
        self.list3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.list4 = [1, 2, 3, 4, 5, 5]
        self.list5 = [0, 2, 4, 7, 9, 15, 22]

    def test_list1(self):
        self.assertEqual(duplicates(self.list1), True)

    def test_list2(self):
        self.assertEqual(duplicates(self.list2), False)

    def test_list3(self):
        self.assertEqual(duplicates(self.list3), True)

    def test_list4(self):
        self.assertEqual(duplicates(self.list4), True)

    def test_list5(self):
        self.assertEqual(duplicates(self.list5), False)


if __name__ == '__main__':
    unittest.main()
