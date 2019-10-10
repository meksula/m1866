import unittest
from m1866_lib.cli.Context import mv_resource


class TestContext(unittest.TestCase):

    def test_mv_resource(self):
        file_path = '/gunpowder.json'
        target = 'global/templates'

        print(mv_resource(file_path, target))

    def test_mv_resource_config_yml(self):
        file_path = 'config.yml'
        target = ''

        print(mv_resource(file_path, target))
