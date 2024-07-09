import unittest
from unittest.mock import patch

from load_test.load_tester import LoadTester


class TestLoadTester(unittest.TestCase):

    def set_up(self, request_type):
        self.url = "http://example.com"
        self.qps = 10
        self.request_type = request_type
        self.threads = 5
        self.data = {'key': 'value'}
        self.load_tester = LoadTester(self.url, self.qps, self.request_type, self.threads, self.data)

    @patch('requests.get')
    def test_send_request_success_get(self, mock_get):
        self.set_up("GET")
        # Set up the mock response
        mock_get.return_value.status_code = 200
        mock_get.return_value.elapsed.total_seconds.return_value = 0.1

        res = self.load_tester._send_request(self.url, self.request_type, self.data, 1.0 / self.qps)

        self.assertEqual(res.get('succeed_request'), 1)
        self.assertEqual(res.get('failed_request'), 0)

    @patch('requests.get')
    def test_send_request_error_get(self, mock_get):
        self.set_up("GET")
        mock_get.return_value.status_code = 500
        mock_get.return_value.elapsed.total_seconds.return_value = 0.1

        res = self.load_tester._send_request(self.url, self.request_type, self.data, 1.0 / self.qps)

        self.assertEqual(res.get('succeed_request'), 0)
        self.assertEqual(res.get('failed_request'), 1)

    @patch('requests.post')
    def test_send_request_success_post(self, mock_post):
        self.set_up("POST")
        mock_post.return_value.status_code = 200
        mock_post.return_value.elapsed.total_seconds.return_value = 0.1

        res = self.load_tester._send_request(self.url, self.request_type, self.data, 1.0 / self.qps)

        self.assertEqual(res.get('succeed_request'), 1)
        self.assertEqual(res.get('failed_request'), 0)

    @patch('requests.post')
    def test_send_request_error_post(self, mock_post):
        self.set_up("POST")
        mock_post.return_value.status_code = 500
        mock_post.return_value.elapsed.total_seconds.return_value = 0.1

        res = self.load_tester._send_request(self.url, self.request_type, self.data, 1.0 / self.qps)

        self.assertEqual(res.get('succeed_request'), 0)
        self.assertEqual(res.get('failed_request'), 1)


if __name__ == '__main__':
    unittest.main()
