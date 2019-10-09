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
        cmd_tpl = self.args_extract(last_command)
        try:
            commands[cmd_tpl[0].strip()]((self.lib_facade, cmd_tpl[1]))
        except KeyError:
            if len(last_command.strip()) > 0:
                print(Fore.RED, f'Command `{last_command}` is not recognized', end=Style.RESET_ALL + '\n')
            else:
                return

    # This function returns entered command as command and arguments
    def args_extract(self, last_command):
        parts = last_command.split('->')
        if len(parts) > 1:
            return parts[0].strip(), parts[1].strip()
        else:
            return last_command.strip(), ''

    def print_info(self):
        print("yml object: " + str(self.config_yml) + "\nOS: " + self.running_os)
