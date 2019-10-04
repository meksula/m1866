from m1866_lib.cli.workspace import create_workspace_dir, list_workspaces

exit_command = 'exit'

# Notice that to invoke most of method in `command` dictionary
# you have to pass instance of class `LibFacade` as argument
commands = {
    # general functions
    'exit': lambda _: say_bay(),
    'help': lambda _: help(),

    'delete workspace': lambda lib_facade: delete_workspace(),

    # magazine API
    'reload': lambda lib_facade: lib_facade[0].reload_hub(),
    'hub list': lambda lib_facade: lib_facade[0].list_coll_hub(),

    # shoots API
    'run vol': lambda _, lib_facade: lib_facade[0].execute_volatile_shoot(),
    'add shoot': lambda lib_facade: lib_facade[0].add_shoot(),
    'run': lambda lib_facade, ref = 'placeholder': lib_facade[0].execute_shoot(ref),
    'run blind': lambda lib_facade, ref: lib_facade[0].execute_shoot_no_hist(),
    'delete': lambda lib_facade, _id: lib_facade[0].delete_shoot(_id),
    'edit': lambda lib_facade: lib_facade[0].edit_shoot(),
    'list': lambda lib_facade: lib_facade[0].list_shoots(),

    # gunpowder API
    'add gunpowder' or 'add g': lambda lib_facade: lib_facade[0].add_gunpowder(),

    # integration_tests API
    'integration prepare': lambda lib_facade: lib_facade[0].prepare_integration(),
    'integration execute': lambda lib_facade: lib_facade[0].execute_integration(),

    # history API
    'history show': lambda lib_facade: lib_facade[0].show_history(),
    'history clear': lambda lib_facade: lib_facade[0].clear_history(),

    # configuration API
    'workspace create': lambda lib_facade: lib_facade[0].create_workspace(),
    'workspace change': lambda lib_facade: lib_facade[0].change_workspace(),
    'workspace migrate': lambda lib_facade: lib_facade[0].migrate_workspace(),
    'workspace show': lambda lib_facade: lib_facade[0].show_workspace(),
    'workspace list': lambda lib_facade: list_workspaces(),

    # postman API
    'postman parse': lambda lib_facade: lib_facade[0].parse_postman_coll(),
    'postman export': lambda lib_facade: lib_facade[0].export_to_postman_coll(),

    # cURL API
    'curl parse': lambda lib_facade: lib_facade[0].parse_curl_coll(),
    'curl export': lambda lib_facade: lib_facade[0].export_to_curl_scripts(),
}


def delete_workspace():
    pass


def help():
    print('Help page')


def say_bay():
    print('Bye!')
