import subprocess
import os
import sys
from colorama import init, Fore, Style
from yaml import safe_load, YAMLError

from m1866_lib.cli.main_controller import MainFlowController
from m1866_lib.cli.unix_utils import define_workspace_path_unix
from m1866_lib.cli.workspace import Workspace


def run():
    init()
    config_file = load_config_yml()
    running_os = os_detect_and_create_workspace()
    print('M1866 v' + str(config_file['settings']['global']['version']) + ' initialized with success and ready to work'
                                                                          '\nType `help` if you want to learn more\n')
    # Initialize workspace from config.yml
    Workspace(config_file['settings']['global']['workspace']['default'])
    MainFlowController(config_file, running_os).flow_init()


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
    if str(os_type).__contains__('Linux') or str(os_type).__contains__('Darwin'):
        workspace_path = define_workspace_path_unix()
        workspace_dir_create(workspace_path)
        create_config(workspace_path)
        return 'unix'
    else:
        print(Fore.RED + 'Sorry, your OS is not supported by m1866 by now')
        sys.exit()


def create_config(workspace_path):
    file_name = 'config.yml'
    complete = workspace_path + '/' + file_name
    try:
        config_file_path = subprocess.check_output('ls ' + workspace_path, shell=True)
        if str(config_file_path).__contains__(file_name):
            print(Fore.GREEN + f'{file_name} detected correctly.')
            print(Style.RESET_ALL)
        else:
            print(f'{file_name} creation')
            mv_resource('config.yml', '')
        create_utils_dirs(workspace_path)
    except FileNotFoundError:
        print(Fore.RED + f'm1866 meets problem with creation config.yml file.'
              f'\nPlease fix problem or execute this command by yourself:'
              f'\n${complete}')
        print(Style.RESET_ALL)


def load_config_yml():
    stream = None
    try:
        stream = open(define_workspace_path_unix() + '/config.yml', 'r')
    except FileNotFoundError:
        stream = open(default_yml_path(), 'r')

    def parse_yml():
        try:
            return safe_load(stream)
        except YAMLError as err:
            return err
    return parse_yml()


def pwd():
    return subprocess.check_output('pwd', shell=True)


def lib_path():
    return str(pwd())[2:-12]


def default_yml_path():
    return lib_path() + 'resources/config.yml'


def version_extract():
    config_file = load_config_yml()
    if config_file is None:
        return 'Undefined'
    return str(config_file['settings']['global']['version'])


def refresh_context():
    _ = subprocess.call("clear", shell=True)


# Add here to `dirs` list all directories you want to create
def create_utils_dirs(workspace_path):
    dirs = ['workspaces', 'global', 'global/templates', 'scripts']

    ls_output = str(subprocess.check_output('ls ' + workspace_path, shell=True))
    for dir_name in dirs:
        if not ls_output.__contains__(dir_name):
            os.system('mkdir ' + workspace_path + '/' + dir_name)
    create_utils_files(workspace_path)


# Add here tuple to `files` list all files to move to current user's workspace
# First variable in tuple act as file name (if file is placed in resource directory, you can type only filename)
# Second variable in tuple act as target directory in your workspace
def create_utils_files(workspace_path):
    files = [
        ('gunpowder.json', 'global/templates'),
        ('shoot.json', 'global/templates')
    ]
    for file_path, target_path in files:
        mv_resource(file_path, target_path, workspace_path)


def mv_resource(file_path, target_path, workspace_path=define_workspace_path_unix()):
    if workspace_path[-1] != '/':
        workspace_path = workspace_path + '/'
    if file_path[0] != '/':
        file_path = '/' + file_path

    cp_source = lib_path() + 'resources' + file_path
    cp_target = workspace_path + target_path
    command = 'cp ' + cp_source + " " + cp_target
    os.system(command)
    return command
