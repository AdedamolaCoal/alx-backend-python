#!/usr/bin/env python3
"""
Unit test module for utils.access_nested_map function.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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

    @parameterized.expand(
        [
            ({}, ("a",), "a"),
            ({"a": 1}, ("a", "b"), "b"),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, missing_key):
        """Test access_nested_map raises KeyError with appropriate message for missing keys."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{missing_key}'")


class TestGetJson(unittest.TestCase):
    """Tests get_json function with mocked HTTP responses."""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns correct payload from mocked requests.get."""
        # mock to return a response with the specified JSON payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests memoize decorator to ensure it caches method results."""

    def test_memoize(self):
        """Test that memoize decorator caches the result of a_method."""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Mock a_method to track how many times it's called
        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            test_instance = TestClass()

            # Call a_property twice
            first_call = test_instance.a_property
            second_call = test_instance.a_property

            # Check the correct result is returned
            self.assertEqual(first_call, 42)
            self.assertEqual(second_call, 42)

            # Ensure a_method was only called once due to memoization
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()