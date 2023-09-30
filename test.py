import unittest

class TestExample(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(1, 1)


    def test_example2(self):
        self.assertEqual(0, 0)


if __name__ == '__main__':
    unittest.main()