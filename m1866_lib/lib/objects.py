# This method has 3 params:
# - from_rsrcs - switches between loading request from resources in .m1866 directory
# and passing arguments in interactive mode
# - id - is zero as default. If you want to load request from resources you have to choose correct id
# - gunpowder - by this parameter you can pass request directly


def factorize(from_rsrcs=False, id=0, gunpowder=None):
    if from_rsrcs is True:
        # todo
        # ładuj plik z jsona w kolekcjach
        pass
    else:
        if valid(gunpowder) is True:
            # todo
            # załaduj i zwróć gunpowder podany w argumencie
            pass
        pass


def valid(gunpowder):
    # todo
    pass


class Gunpowder:

    def __init__(self, auth_type, headers, body, params):
        self.auth_type = auth_type
        self.headers = headers
        self.body = body
        self.params = params

    def info(self):
        pass
