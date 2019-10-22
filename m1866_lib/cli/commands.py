from m1866_lib.cli.interact import UserInteractor

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

    'delete workspace': lambda fargs: fargs[0].instance.delete_workspace(fargs[1]),

    # magazine API
    'reload': lambda fargs: fargs[0].instance.reload_hub(),
    'hub list': lambda fargs: fargs[0].instance.list_coll_hub(),

    # shoots API
    'run vol': lambda fargs: fargs[0].instance.execute_volatile_shoot(),
    'add shoot': lambda fargs: fargs[0].instance.add_shoot(fargs[1]),
    'run': lambda fargs = 'placeholder': fargs[0].instance.execute_shoot(fargs[1]),
    'run blind': lambda fargs: fargs[0].instance.execute_shoot_no_hist(),
    'delete': lambda fargs: fargs[0].instance.delete_shoot(fargs[1]),
    'edit': lambda fargs: fargs[0].instance.edit_shoot(),
    'list': lambda fargs: fargs[0].instance.list_shoots(),

    # gunpowder API
    'add gunpowder' or 'add g': lambda fargs: fargs[0].instance.add_gunpowder(),

    # integration_tests API
    'integration prepare': lambda fargs: fargs[0].instance.prepare_integration(),
    'integration execute': lambda fargs: fargs[0].instance.execute_integration(),

    # history API
    'history show': lambda fargs: fargs[0].instance.show_history(),
    'history clear': lambda fargs: fargs[0].instance.clear_history(),

    # configuration API
    'workspace create': lambda fargs: fargs[0].instance.create_workspace(),
    'workspace change': lambda fargs: fargs[0].change_workspace(),
    'workspace migrate': lambda fargs: fargs[0].migrate_workspace(),
    'workspace show': lambda fargs: fargs[0].show_workspace(),
    'show': lambda fargs: fargs[0].show_workspace(),
    'workspace list': lambda fargs: fargs[0].print_workspaces_list(),
    'workspace use': lambda fargs: fargs[0].use_workspace(fargs[1][0][0]),

    # postman API
    'postman parse': lambda fargs: fargs[0].parse_postman_coll(),
    'postman export': lambda fargs: fargs[0].export_to_postman_coll(),

    # cURL API
    'curl parse': lambda fargs: fargs[0].parse_curl_coll(),
    'curl export': lambda fargs: fargs[0].export_to_curl_scripts(),

    # user interacts
    'y': lambda fargs: UserInteractor('y'),
    'n': lambda fargs: UserInteractor('n'),

    'Y': lambda fargs: UserInteractor('y'),
    'N': lambda fargs: UserInteractor('n'),

    # useful in debug of user's input, check last boolean input
    'last': lambda fargs: print(UserInteractor('last').get_last())
}


def help():
    print('Help page')


def tutor(args):
    if args is None:
        return
    print('Tutor ' + args)


def say_bay():
    print('Bye!')
