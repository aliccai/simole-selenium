import unittest
from Calculator import calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('start')

    def tearDown(self) -> None:
        print('end')

    def test_add(self):
        c = calculator(3, 5)
        result = c.add()
        self.assertEqual(result, 8)

    def test_mul(self):
        c = calculator(3, 3)
        result = c.mul()
        self.assertEqual(result, 10)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(MyTestCase("test_add"))
    suit.addTest(MyTestCase("test_mul"))

    runner = unittest.TextTestRunner()
    runner.run(suit)
