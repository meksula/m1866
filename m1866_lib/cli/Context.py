import subprocess
import os
import sys
from colorama import init, Fore, Style


def run():
    init()
    os_detect_and_create_workspace()


def define_workspace_path_linux():
    delimiter = '/'
    current_dir = subprocess.check_output('pwd')
    path_parts = str(current_dir).split('/')
    return delimiter + path_parts[1] + delimiter + path_parts[2] + delimiter + '.m1866'


def workspace_dir_create(workspace_path):
    confirm = 'exist'
    command = '[ -d "' + workspace_path + '" ] && echo "' + confirm + '"'
    is_exist = ''
    try:
        is_exist = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError:
        try:
            os.system('mkdir ' + workspace_path)
            print('Correctly created workspace here: ' + workspace_path)
        except:
            print(Fore.RED + 'Application has no right to make new directory here in your home directory: '
                  + workspace_path)
    if str(is_exist)[2:7] == 'exist':
        print(Fore.GREEN + 'Workspace detected correctly.')
        print(Style.RESET_ALL)
    return workspace_path


def os_detect_and_create_workspace():
    os_type = subprocess.check_output('uname')
    if str(os_type).__contains__('Linux'):
        workspace_path = define_workspace_path_linux()
        workspace_dir_create(workspace_path)
        create_config(workspace_path)
        return
    if str(os_type).__contains__('Darwin'):
        print(Fore.RED + 'OS X is not supported yet, but it will be soon')
        print(Style.RESET_ALL)
        return
    else:
        print(Fore.RED + 'Sorry, your OS is not supported by m1866 by now')
        sys.exit()


def create_config(workspace_path):
    file_name = 'config.yml'
    complete = workspace_path + '/' + file_name
    try:
        config_file = subprocess.check_output('ls ' + workspace_path, shell=True)
        if str(config_file).__contains__(file_name):
            print(Fore.GREEN + f'{file_name} detected correctly')
            print(Style.RESET_ALL)
        else:
            print(f'{file_name} creation')
            read_config_yml(workspace_path + '/')
    except FileNotFoundError:
        print(Fore.RED + f'm1866 meets problem with creation config.yml file.'
              f'\nPlease fix problem or execute this command by yourself:'
              f'\n${complete}')
        print(Style.RESET_ALL)


def read_config_yml(workspace_path):
    config_yml_path = subprocess.check_output('pwd', shell=True)
    os.system('cp ' + str(config_yml_path)[2:-12] + 'resources/config.yml ' + workspace_path)
