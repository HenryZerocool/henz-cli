import unittest
from unittest.mock import patch
from henzcli import __main__


class Flags(unittest.TestCase):
    def test_good_flag(self):
        self.assertEqual(__main__.goodBad("--good"), 1)

    def test_bad_flag(self):
        self.assertEqual(__main__.goodBad("--bad"), 2)

    def test_empty_flag(self):
        self.assertEqual(__main__.goodBad(""), 0)


class URLResponse(unittest.TestCase):
    @patch('henzcli.__main__.requests.head')
    def test_url_ok(self, mock_get):
        url = "https://google.com/"
        mock_get.return_value.status_code = 200
        status = __main__.getRequestStatus(url)
        self.assertEqual(status, 200)

    @patch('henzcli.__main__.requests.get')
    def test_url_error(self, mock_get):
        url = "https://google.com/"
        mock_get.return_value.status_code = 404
        status = __main__.getRequestStatus(url)
        self.assertEqual(status, 404)


if __name__ == '__main__':
    unittest.main()
