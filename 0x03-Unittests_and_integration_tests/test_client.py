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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the correct list of repos."""
        mock_repos_payload = [{"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"}]
        mock_get_json.return_value = mock_repos_payload

        with patch(
            "client.GithubOrgClient._public_repos_url", new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/test-org/repos"
            )

            client = GithubOrgClient("test-org")

            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(client.public_repos(), expected_repos)

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test-org/repos"
            )

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
            ({"license": None}, "my_license", False),  # Edge case: No license info
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the correct boolean based on the license key."""
        client = GithubOrgClient("test-org")
        self.assertEqual(client.has_license(repo, license_key), expected)


if __name__ == "__main__":
    unittest.main()
