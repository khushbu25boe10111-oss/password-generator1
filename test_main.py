import unittest
import string
from main import *

class TestPasswordGenerator(unittest.TestCase):

    def test_length(self):
        length = 10
        password = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        self.assertEqual(len(password), length)

    def test_contains_letters(self):
        password = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        self.assertTrue(any(c.isalpha() for c in password))

if __name__ == "__main__":
    unittest.main()