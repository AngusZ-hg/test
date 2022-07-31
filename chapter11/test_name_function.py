import unittest
import sys
sys.path.append('..')
from chapter10.remember_me import get_stored_username
from name_function import get_formatted_name

get_stored_username()
# print(sys.path)

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()

