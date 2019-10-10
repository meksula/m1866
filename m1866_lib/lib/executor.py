import requests
from colorama import Fore, Style

from m1866_lib.lib.objects import Smoke

http_methods = {
    "get": lambda shoot: http_get(shoot),
    "post": lambda shoot: http_post(shoot)
}


def execute_request(shoot):
    shoot = pre_valid(shoot)
    if shoot is not None:
        resp = http_methods[shoot["http_method"]](shoot)
        return Smoke(shoot, resp.content, resp.cookies, resp.headers, resp.status_code, resp.url)
    else:
        print(Fore.RED, 'Your request is invalid', Style.RESET_ALL)


def pre_valid(shoot):
    # TODO
    return shoot


def http_get(shoot):
    # TODO
    url = build_url(shoot)
    return requests.get(url)


def http_post(shoot):
    pass


def build_url(shoot):
    # TODO
    url = shoot["url"]
    return url["protocol"] + "://" + url["domain"] + url["uri"]
