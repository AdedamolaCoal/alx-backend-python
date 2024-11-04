#!/usr/bin/env python3
"""
Unit test module for client.GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, PropertyMock
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

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the correct URL based on org data."""
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test-org/repos"
        }

        client = GithubOrgClient("test-org")

        self.assertEqual(
            client._public_repos_url, "https://api.github.com/orgs/test-org/repos"
        )


if __name__ == "__main__":
    unittest.main()
