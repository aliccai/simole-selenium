from Calculator import calculator
import unittest


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('up')

    def tearDown(self) -> None:
        print('down')

    def test_add(self):
        c = calculator(2, 5)
        res = 7
        self.assertEqual(c.add(), res)

    def test_mul(self):
        c = calculator(3, 6)
        res = 18
        self.assertEqual(c.mul(), res)


if __name__ == '__main':
    suite = unittest.TestSuite()
    suite.addTest(TestCase('test_add'))
    suite.addTest(TestCase('test_mul'))

    runner = unittest.TestRunner()
    runner.run(suite)
