import unittest

from greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_with_name(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")


if __name__ == "__main__":
    unittest.main()
