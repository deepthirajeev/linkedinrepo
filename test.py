import unittest
from main import main


class TestStringMethods(unittest.TestCase):

    # Returns True if the string contains 4 a.
    def test_strings_a(self):
        main.linked_in_login()

if __name__ == '__main__':
    unittest.main()