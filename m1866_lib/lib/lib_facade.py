# This facade class represents all entry points of main, core library.
from m1866_lib.cli.workspace import Workspace


class LibFacade:

    def __init__(self):
        self.workspace = Workspace.instance

    # magazine API
    def reload_hub(self):
        pass

    def list_coll_hub(self):
        pass

    # shoots API
    def execute_volatile_shoot(self):
        pass

    def add_shoot(self, options):
        pass

    def execute_shoot(self, options):
        for opt in options:
            print(str(opt))

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
        self.workspace.create_workspace_dir(input('Type workspace name: '))

    def change_workspace(self):
        pass

    def migrate_workspace(self):
        pass

    def show_workspace(self):
        self.workspace.show_workspace()

    def print_workspaces_list(self):
        self.workspace.print_workspaces_list()

    def use_workspace(self, workspace_name):
        self.workspace.use_workspace(workspace_name)

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
