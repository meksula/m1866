import os
import subprocess
from colorama import Fore, Back, Style
import re

from m1866_lib.cli.unix_utils import define_workspace_path_unix


def create_workspace_dir(workspace_name):
    if not valid(workspace_name):
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


def valid(workspace_name):
    regex = re.compile(r"^[a-zA-Z0-9_]+$")
    result = regex.match(workspace_name)
    return result is not None


def list_workspaces():
    workspace_path = define_workspace_path_unix() + '/workspaces'
    ls_output = str(subprocess.check_output('ls ' + workspace_path, shell=True))
    dir_list = ls_output.strip()[2:-1].split('\\n')
    if len(dir_list[:-1]) > 0:
        print('\nWorkspaces:')
        for dir_name in sorted(dir_list[:-1], key=len):
            print('* ' + Back.CYAN, dir_name, Style.RESET_ALL)
    else:
        print(Fore.RED, 'There is no workspaces yet', Style.RESET_ALL)
