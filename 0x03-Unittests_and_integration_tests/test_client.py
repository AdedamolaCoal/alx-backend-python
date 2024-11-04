#!/usr/bin/env python3
"""
Unit test module for client.GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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


@parameterized_class(
    [
        {
            "org_payload": org_payload,
            "repos_payload": repos_payload,
            "expected_repos": expected_repos,
            "apache2_repos": apache2_repos,
        },
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos."""

    @classmethod
    def setUpClass(cls):
        """Set up the class with a patched requests.get to simulate external API calls."""
        # Start patching requests.get
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        # Define side effects for different URLs to return appropriate fixture data
        cls.mock_get.side_effect = cls.get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down the class by stopping the patcher."""
        cls.get_patcher.stop()

    @staticmethod
    def get_json_side_effect(url):
        """Side effect function to return different data based on the requested URL."""
        if url == "https://api.github.com/orgs/test-org":
            return org_payload
        elif url == "https://api.github.com/orgs/test-org/repos":
            return repos_payload
        return {}

    # def test_public_repos(self):
    #     """Test public_repos to ensure it returns expected repositories."""
    #     client = GithubOrgClient("test-org")
    #     self.assertEqual(client.public_repos(), self.expected_repos)

    @classmethod
    def _mock_get(cls, url):
        if url == "https://api.github.com/orgs/google":
            return cls._mock_response(cls.org_payload)
        elif url == "https://api.github.com/orgs/google/repos":
            return cls._mock_response(cls.repos_payload)
        return cls._mock_response({})  # Return an empty response for unexpected URLs

    @staticmethod
    def _mock_response(data):
        """Create a mock response object."""

        class MockResponse:
            def json(self):
                return data

        return MockResponse()

    def test_public_repos(self):
        """Test the public_repos method."""
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license argument."""
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
