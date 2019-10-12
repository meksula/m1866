import requests
from colorama import Fore, Style

from m1866_lib.lib.history import History
from m1866_lib.lib.objects import Smoke


http_methods = {
    "get": lambda shoot: http_get(shoot),
    "post": lambda shoot: http_post(shoot),
    "put": lambda shoot: http_put(shoot),
    "patch": lambda shoot: http_patch(shoot),
    "delete": lambda shoot: http_delete(shoot)
}


def execute_request(shoot):
    if shoot is not None:
        resp = http_methods[shoot["http_method"]](shoot)
        smoke = Smoke(shoot, resp.content, resp.cookies, resp.headers, resp.status_code, resp.url)
        if 'store_history' in shoot.keys() and shoot['store_history'] is True:
            History().save(smoke)
            return smoke
        return smoke
    else:
        print(Fore.RED, 'Your request is invalid', Style.RESET_ALL)


# Shoot input object must be validated before execute request
# You will receive information about validation errors etc.
def pre_valid(shoot):
    return shoot


def http_get(shoot):
    shoot = pre_valid(shoot)
    url = build_url(shoot)
    return requests.get(url)


def http_post(shoot):
    shoot = pre_valid(shoot)
    pass


def http_put(shoot):
    shoot = pre_valid(shoot)
    pass


def http_patch(shoot):
    shoot = pre_valid(shoot)
    pass


def http_delete(shoot):
    shoot = pre_valid(shoot)
    pass


def build_url(shoot):
    url = shoot["url"]
    keys = url.keys()

    def compose(domain):
        # Default placeholder syntax:
        # ${param} - this will be replaced with provided parameters in list shoot.url.params
        # Param must have two fields: `key` and `value`
        def params_attach(complete_url):
            try:
                param_list = shoot["url"]["params"]
                for param in param_list:
                    old = '${' + param["key"] + '}'
                    new = param["value"]
                    complete_url = complete_url.replace(old, new)
                return complete_url
            except KeyError:
                return complete_url
        protocol = 'http'
        uri = '/'
        if "protocol" in keys:
            protocol = url["protocol"]
        if "uri" in keys:
            uri = url["uri"]
        return params_attach(protocol + "://" + domain + uri)

    if "domain" not in keys and "ip" not in keys:
        print(Fore.RED, 'Both domain name and IPv4 address is not specified!', Style.RESET_ALL)
    if "domain" in keys:
        return compose(url["domain"])
    else:
        if "ip" in keys:
            return compose(url["ip"])
