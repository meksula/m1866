import os
import subprocess
from colorama import Fore, Back, Style
import re

from m1866_lib.cli.interact import UserInteractor
from m1866_lib.cli.unix_utils import define_workspace_path_unix


class Workspace:
    instance = None

    def __init__(self, default_workspace):
        if not Workspace.instance:
            Workspace.instance = Workspace.__Workspace(default_workspace)
        else:
            Workspace.instance.current_workspace = default_workspace
        self.valid_workspace(default_workspace)

    def valid_workspace(self, default_workspace):
        if default_workspace is None:
            print(Fore.RED, 'Cannot read default workspace from config.yml file. Set `default` parameter', Style.RESET_ALL)
            return
        if default_workspace not in self.instance.list_workspaces():
            print(Fore.RED, f'Workspace called: {default_workspace} not recognized!', Style.RESET_ALL)
            self.instance.create_workspace_dir_prompt(default_workspace)
        return default_workspace

    def workspace_establish(self, workspace):
        if workspace in self.instance.list_workspaces():
            self.instance.use_workspace(workspace)
            return
        elif workspace is not None and workspace is not 'None' and workspace.strip() is not '':
            self.instance.create_workspace_dir(workspace)
            self.instance.use_workspace(workspace)

    def is_workspace_established(self):
        return self.instance.current_workspace is not None

    class __Workspace:
        def __init__(self, workspace):
            self.current_workspace = workspace

        # Can create workspace only with user's confirmation
        def create_workspace_dir_prompt(self, default_workspace):
            print(f'Do create {default_workspace} workspace now? (Y/N)')
            result = UserInteractor(input()).get_last()
            if result is True:
                self.create_workspace_dir(default_workspace)
            else:
                print(Fore.RED, 'Workspace not established.', Style.RESET_ALL)
            return

        def create_workspace_dir(self, workspace_name):
            if not self.valid(workspace_name):
                print(Fore.RED, 'Workspace was not created because name is not valid!', Style.RESET_ALL)
                return
            workspace_path = define_workspace_path_unix() + '/workspaces/' + workspace_name

            def inner_dirs():
                for dir_name in ['shoots', 'gunpowder', 'history', 'integration']:
                    os.system('mkdir ' + workspace_path + '/' + dir_name)

            try:
                subprocess.check_output('ls ' + workspace_path)
                return
            except FileNotFoundError:
                try:
                    subprocess.check_output('ls ' + workspace_path, shell=True)
                    print(Fore.RED, f'Workspace called `{workspace_name}` just exist!')
                except subprocess.CalledProcessError:
                    os.system('mkdir ' + workspace_path)
                    inner_dirs()
                    print(Fore.GREEN, f'`{workspace_name}` workspace created')
            finally:
                print(Style.RESET_ALL)

        def load_workspace(self, workspace_name):
            if workspace_name is None:
                print(Fore.RED, 'Workspace is not defined!\nUse command `workspace use WORKSPACE_NAME`',
                      Style.RESET_ALL)

        def workspace_pointer(self):
            return define_workspace_path_unix() + '/workspaces/' + self.current_workspace

        def valid(self, workspace_name):
            regex = re.compile(r"^[a-zA-Z0-9_]+$")
            result = regex.match(workspace_name)
            return result is not None

        def list_workspaces(self):
            workspace_path = define_workspace_path_unix() + '/workspaces'
            ls_output = str(subprocess.check_output('ls ' + workspace_path, shell=True))
            return ls_output.strip()[2:-1].split('\\n')

        def print_workspaces_list(self):
            dir_list = self.list_workspaces()
            if len(dir_list[:-1]) > 0:
                print('\nWorkspaces:')
                for dir_name in sorted(dir_list[:-1], key=len):
                    if dir_name == self.current_workspace:
                        print('* ' + Back.CYAN, dir_name, Style.RESET_ALL, '  <- current workspace')
                    else:
                        print('* ' + Back.CYAN, dir_name, Style.RESET_ALL)
            else:
                print(Fore.RED, 'There is no workspaces yet', Style.RESET_ALL)

        def use_workspace(self, workspace_name):
            def is_workspace_exist():
                if workspace_name in self.list_workspaces():
                    return True
                else:
                    print(Fore.RED, f'Workspace `{workspace_name}` not exist!', Style.RESET_ALL)

            if is_workspace_exist():
                self.current_workspace = workspace_name
                print('Checkout to workspace: ' + self.current_workspace)

        def show_workspace(self):
            if self.current_workspace is None or self.current_workspace == 'None':
                print('Workspace is not set yet')
            else:
                print(f'Current workspace: {self.current_workspace}')
                return self.current_workspace
