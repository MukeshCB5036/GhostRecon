import unittest
from unittest.mock import patch, MagicMock
from ghostrecon.core import get_subdomains_crtsh, resolve_dns, bruteforce_subdomains

class TestCoreFunctions(unittest.TestCase):

    @patch('ghostrecon.core.requests.get')
    def test_get_subdomains_crtsh_success(self, mock_get):
        # Mock crt.sh JSON response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"name_value": "test.example.com\nwww.example.com"},
            {"name_value": "mail.example.com"}
        ]
        mock_get.return_value = mock_response

        subs = get_subdomains_crtsh("example.com")
        self.assertIn("test.example.com", subs)
        self.assertIn("www.example.com", subs)
        self.assertIn("mail.example.com", subs)

    @patch('ghostrecon.core.dns.resolver.resolve')
    def test_resolve_dns_success_and_failure(self, mock_resolve):
        # Mock successful DNS resolution
        mock_answer = MagicMock()
        mock_answer.to_text.return_value = "1.2.3.4"
        mock_resolve.return_value = [mock_answer]

        ip = resolve_dns("test.example.com")
        self.assertEqual(ip, "1.2.3.4")

        # Mock DNS failure
        mock_resolve.side_effect = Exception("DNS failure")
        ip = resolve_dns("fail.example.com")
        self.assertIsNone(ip)

    @patch('ghostrecon.core.resolve_dns')
    @patch('ghostrecon.core.load_wordlist')
    def test_bruteforce_subdomains(self, mock_load_wordlist, mock_resolve_dns):
        mock_load_wordlist.return_value = ['www', 'mail', 'dev']
        mock_resolve_dns.side_effect = lambda sub: "1.2.3.4" if sub == "mail.example.com" else None

        found = bruteforce_subdomains("example.com", "fake_path", limit=None)
        self.assertEqual(found, ["mail.example.com"])

if __name__ == "__main__":
    unittest.main()
