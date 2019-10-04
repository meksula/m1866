import subprocess


def define_workspace_path_unix():
    delimiter = '/'
    current_dir = subprocess.check_output('pwd')
    path_parts = str(current_dir).split('/')
    return delimiter + path_parts[1] + delimiter + path_parts[2] + delimiter + '.m1866'
