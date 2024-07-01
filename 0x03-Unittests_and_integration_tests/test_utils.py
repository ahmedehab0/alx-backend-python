#!/usr/bin/python3
"""tests for the utils.access_nested_map"""


from utils import access_nested_map
import unittest
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, a, b, expected):
        result = access_nested_map(a, b)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
