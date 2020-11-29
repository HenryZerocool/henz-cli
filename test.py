import unittest
from unittest.mock import patch
from main import goodBad, getRequestStatus


class Flags(unittest.TestCase):
    def test_good_flag(self):
        self.assertEqual(goodBad("--good"), 1)

    def test_bad_flag(self):
        self.assertEqual(goodBad("--bad"), 2)

    def test_empty_flag(self):
        self.assertEqual(goodBad(""), 0)


class URLResponse(unittest.TestCase):
    @patch('main.requests.head')
    def test_url_ok(self, mock_get):
        url = "https://google.com/"
        mock_get.return_value.status_code = 200
        status = getRequestStatus(url)
        self.assertEqual(status, 200)

    @patch('main.requests.get')
    def test_url_404(self, mock_get):
        url = "https://google.com/"
        mock_get.return_value.status_code = 404
        status = getRequestStatus(url)
        self.assertEqual(status, 404)

    @patch('main.requests.get')
    def test_url_502(self, mock_get):
        url = "https://google.com/"
        mock_get.return_value.status_code = 502
        status = getRequestStatus(url)
        self.assertEqual(status, 502)


if __name__ == '__main__':
    unittest.main()
