import unittest
from m1866_lib.lib.executor import execute_request


class TestExecutor(unittest.TestCase):

    def test_execute_request(self):
        smoke = execute_request(minimalistic_shoot())
        self.assertIsNotNone(smoke)
        self.assertIsNotNone(smoke.shoot)
        self.assertIsNotNone(smoke.response_body)
        self.assertIsNotNone(smoke.url)
        self.assertIsNotNone(smoke.headers)
        self.assertIsNotNone(smoke.cookies)
        self.assertIsNotNone(smoke.timestamp)
        self.assertIsNotNone(smoke.response_status)
        self.assertEqual(smoke.response_status, 200)
        self.assertEqual(smoke.url, "https://jsonplaceholder.typicode.com/todos/1")


def minimalistic_shoot():
    return {
        "http_method": "get",
        "url": {
            "protocol": "https",
            "domain": "jsonplaceholder.typicode.com",
            "uri": "/todos/1"
        }
    }
