from m1866_lib.cli.workspace import list_workspaces

exit_command = 'exit'

# Notice that to invoke most of method in `command` dictionary
# you have to pass instance of class `LibFacade` as argument in tuple
# So, you need to pass tuple (LibFacade, args) called further as `fargs`
# args in this case act as argument passed in command typed from keyboard
commands = {
    # general functions
    'exit': lambda fargs: say_bay(),
    'help': lambda fargs: help(),
    'tutor': lambda fargs: tutor(fargs[1]),

    'delete workspace': lambda fargs: delete_workspace(),

    # magazine API
    'reload': lambda fargs: fargs[0].reload_hub(),
    'hub list': lambda fargs: fargs[0].list_coll_hub(),

    # shoots API
    'run vol': lambda fargs: fargs[0].execute_volatile_shoot(),
    'add shoot': lambda fargs: fargs[0].add_shoot(),
    'run': lambda fargs = 'placeholder': fargs[0].execute_shoot(fargs[1]),
    'run blind': lambda fargs: fargs[0].execute_shoot_no_hist(),
    'delete': lambda fargs: fargs[0].delete_shoot(fargs[1]),
    'edit': lambda fargs: fargs[0].edit_shoot(),
    'list': lambda fargs: fargs[0].list_shoots(),

    # gunpowder API
    'add gunpowder' or 'add g': lambda fargs: fargs[0].add_gunpowder(),

    # integration_tests API
    'integration prepare': lambda fargs: fargs[0].prepare_integration(),
    'integration execute': lambda fargs: fargs[0].execute_integration(),

    # history API
    'history show': lambda fargs: fargs[0].show_history(),
    'history clear': lambda fargs: fargs[0].clear_history(),

    # configuration API
    'workspace create': lambda fargs: fargs[0].create_workspace(),
    'workspace change': lambda fargs: fargs[0].change_workspace(),
    'workspace migrate': lambda fargs: fargs[0].migrate_workspace(),
    'workspace show': lambda fargs: fargs[0].show_workspace(),
    'workspace list': lambda fargs: list_workspaces(),

    # postman API
    'postman parse': lambda fargs: fargs[0].parse_postman_coll(),
    'postman export': lambda fargs: fargs[0].export_to_postman_coll(),

    # cURL API
    'curl parse': lambda fargs: fargs[0].parse_curl_coll(),
    'curl export': lambda fargs: fargs[0].export_to_curl_scripts(),
}


def delete_workspace():
    pass


def help():
    print('Help page')


def tutor(args):
    if args is None:
        return
    print('Tutor ' + args)


def say_bay():
    print('Bye!')
