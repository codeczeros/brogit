from func import add
import unittest

class FuncTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 4), 6)
    
    def test_add2(self):
        self.assertEqual(add(1, 4), 5)
    
    def test_add3(self):
        self.assertEqual(add(1, 4), 5)


if __name__ == "__main__":
    unittest.main()