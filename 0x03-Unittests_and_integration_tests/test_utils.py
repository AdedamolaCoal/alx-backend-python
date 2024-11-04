#!/usr/bin/env python3
"""
Unit test module for utils.access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map  # Assumes function is in utils.py


class TestAccessNestedMap(unittest.TestCase):
    """Tests access_nested_map function with different inputs and paths."""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns correct value for given nested_map and path."""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
