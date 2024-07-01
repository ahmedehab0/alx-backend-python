#!/usr/bin/env python3
"""tests for the utils.access_nested_map"""


from utils import access_nested_map, get_json
import unittest
from unittest.mock import patch
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """ Class for Testing access_nested_map """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, a, b, expected):
        """test for access_nested_map method"""
        result = access_nested_map(a, b)
        self.assertEqual(result, expected)
    
    @parameterized.expand([
        ({}, ("a", ), 'a'),
        ({"a": 1}, ("a", "b"), 'b')])
    def test_access_nested_map_exception(self, a, b, expected):
        with self.assertRaises(KeyError) as e:
            access_nested_map(a, b)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """Class for testing get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test for the utils.get_json function to check
        that it returns the expected result."""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()
    

    
    
if __name__ == '__main__':
    unittest.main()
