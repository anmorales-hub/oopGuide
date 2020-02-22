import unittest
from examples.abstraction import SquareRoot


class MyTestCase(unittest.TestCase):
    def test_Examples_root(self):
        self.assertEqual(6, SquareRoot.squareRoot(36))
        self.assertEqual(6, SquareRoot.squareRootA(36))



if __name__ == '__main__':
    unittest.main()