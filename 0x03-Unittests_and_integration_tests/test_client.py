#!/usr/bin/env python3
"""
Unit test module for client.GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient.org method."""

    @parameterized.expand(
        [
            ("google", {"login": "google", "id": 1}),
            ("abc", {"login": "abc", "id": 2}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org_name, org_data, mock_get_json):
        """Test that GithubOrgClient.org returns correct organization data."""
        mock_get_json.return_value = org_data

        client = GithubOrgClient(org_name)

        self.assertEqual(client.org, org_data)

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


if __name__ == "__main__":
    unittest.main()
