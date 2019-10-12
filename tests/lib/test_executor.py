import unittest
from m1866_lib.lib.executor import execute_request, build_url

min_url = "https://jsonplaceholder.typicode.com/todos/1"
min_url_ip = "https://172.64.128.28/todos/1"
base_url = "http://172.64.128.28/"


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
        self.assertEqual(smoke.url, min_url)

    def test_build_url(self):
        url = build_url(minimalistic_shoot())
        print(url)
        self.assertEqual(url, min_url)

    def test_build_url_ip(self):
        url = build_url(min_shoot_ip())
        self.assertEqual(url, min_url_ip)

    def test_build_url_both_domain_and_ip_are_not_specified(self):
        shoot = no_domain_and_ip_shoot()
        result_url = build_url(shoot)
        self.assertEqual(result_url, None)

    def test_build_url_with_only_domain_name(self):
        shoot = only_ip_shoot()
        result_url = build_url(shoot)
        self.assertEqual(result_url, base_url)

    def test_build_url_with_one_placeholder(self):
        shoot = one_param_shoot()
        result_url = build_url(shoot)
        self.assertEqual(min_url, result_url)

    def test_build_url_with_multi_placeholders(self):
        shoot = multi_param_shoot()
        result_url = build_url(shoot)
        self.assertEqual(min_url, result_url)


def minimalistic_shoot():
    return {
        "http_method": "get",
        "url": {
            "protocol": "https",
            "domain": "jsonplaceholder.typicode.com",
            "uri": "/todos/1"
        }
    }


def min_shoot_ip():
    return {
        "http_method": "get",
        "url": {
            "protocol": "https",
            "ip": "172.64.128.28",
            "uri": "/todos/1"
        }
    }


def no_domain_and_ip_shoot():
    return {
        "http_method": "get",
        "url": {
            "protocol": "https",
            "uri": "/todos/1"
        }
    }


def only_ip_shoot():
    return {
        "http_method": "get",
        "url": {
            "ip": "172.64.128.28",
        }
    }


def one_param_shoot():
    return {
        "http_method": "get",
        "url": {
            "protocol": "https",
            "domain": "jsonplaceholder.typicode.com",
            "uri": "/${example_param}/1",
            "params": [
                {
                    "key": "example_param",
                    "value": "todos"
                }
            ]
        }
    }


def multi_param_shoot():
    return {
        "http_method": "get",
        "url": {
            "protocol": "https",
            "domain": "jsonplaceholder.typicode.com",
            "uri": "/${example_param}/${example_param_2}",
            "params": [
                {
                    "key": "example_param",
                    "value": "todos"
                },
                {
                    "key": "example_param_2",
                    "value": "1"
                }
            ]
        }
    }