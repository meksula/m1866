from m1866_lib.cli.commands import commands, exit_command
from colorama import Fore, Style
from m1866_lib.lib.lib_facade import LibFacade


def prompt():
    print('> ', end='')
    return input()


class MainFlowController:

    def __init__(self, config_yml, running_os):
        self.config_yml = config_yml
        self.running_os = running_os
        self.load_alises(config_yml)
        self.lib_facade = LibFacade()

    def flow_init(self):
        if (self.config_yml is not None) and (self.running_os is not None):
            self.main_event_loop()

    def load_alises(self, config_yml):
        def no_aliases():
            print('No aliases detected')
        try:
            aliases = config_yml['aliases']
            if len(aliases) > 0:
                for alias_key in aliases:
                    commands[alias_key] = aliases[alias_key]
            else:
                no_aliases()
        except KeyError:
            no_aliases()

    def main_event_loop(self):
        last_command = ''
        while last_command.lower() != exit_command:
            last_command = prompt()
            self.execute(last_command)
        return

    def execute(self, last_command):
        try:
            commands[last_command.strip()]((self.lib_facade, last_command))
        except KeyError:
            if len(last_command.strip()) > 0:
                print(Fore.RED, f'Command `{last_command}` is not recognized', end=Style.RESET_ALL + '\n')
            else:
                return

    def print_info(self):
        print("yml object: " + str(self.config_yml) + "\nOS: " + self.running_os)
