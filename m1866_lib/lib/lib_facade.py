# This facade class represents all entry points of main, core library.
from m1866_lib.cli.workspace import create_workspace_dir
from m1866_lib.lib.shoots_commons import MagazineFacade, ShootsFacade, GunpowderFacade, IntegrationFacade, \
    HistoryFacade, ConfigurationFacade, PostmanFacade, CurlFacade


class LibFacade:

    def __init__(self):
        self.magazineFacade = MagazineFacade()
        self.shootsFacade = ShootsFacade()
        self.gunpowderFacade = GunpowderFacade()
        self.integrationTestFacade = IntegrationFacade()
        self.historyFacade = HistoryFacade()
        self.configurationFacade = ConfigurationFacade()
        self.postmanFacade = PostmanFacade()
        self.curlFacade = CurlFacade()

    # magazine API
    def reload_hub(self):
        pass

    def list_coll_hub(self):
        pass

    # shoots API
    def execute_volatile_shoot(self):
        pass

    def add_shoot(self):
        pass

    def execute_shoot(self):
        pass

    def execute_shoot_no_hist(self):
        pass

    def delete_shoot(self):
        pass

    def edit_shoot(self):
        pass

    def list_shoots(self):
        pass

    # gunpowder API
    def add_gunpowder(self):
        print('Add gunpowder is running')
        pass

    # integration_tests API
    def prepare_integration(self):
        pass

    def execute_integration(self):
        pass

    # history API
    def show_history(self):
        pass

    def clear_history(self):
        pass

    # configuration API
    def create_workspace(self):
        create_workspace_dir(input('Type workspace name: '))
        pass

    def change_workspace(self):
        pass

    def migrate_workspace(self):
        pass

    def show_workspace(self):
        pass

    # postman API
    def parse_postman_coll(self):
        pass

    def export_to_postman_coll(self):
        pass

    # cURL API
    def parse_curl_coll(self):
        pass

    def export_to_curl_scripts(self):
        pass
