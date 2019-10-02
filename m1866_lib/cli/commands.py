exit_command = 'exit'

# Notice that to invoke most of method in `command` dictionary
# you have to pass instance of class `LibFacade` as argument
commands = {
    # general functions
    'exit': lambda _: say_bay(),
    'help': lambda _: help(),

    # magazine API
    'reload': lambda lib_facade: lib_facade.reload_hub(),
    'hub list': lambda lib_facade: lib_facade.list_coll_hub(),

    # shoots API
    'run vol': lambda _, lib_facade: lib_facade.execute_volatile_shoot(),
    'add shoot': lambda lib_facade: lib_facade.add_shoot(),
    'run': lambda lib_facade, ref = 'placeholder': lib_facade.execute_shoot(ref),
    'run blind': lambda lib_facade, ref: lib_facade.execute_shoot_no_hist(),
    'delete': lambda lib_facade, _id: lib_facade.delete_shoot(_id),
    'edit': lambda lib_facade: lib_facade.edit_shoot(),
    'list': lambda lib_facade: lib_facade.list_shoots(),

    # gunpowder API
    'add gunpowder' or 'add g': lambda lib_facade: lib_facade.add_gunpowder(),

    # integration_tests API
    'integration prepare': lambda lib_facade: lib_facade.prepare_integration(),
    'integration execute': lambda lib_facade: lib_facade.execute_integration(),

    # history API
    'history show': lambda lib_facade: lib_facade.show_history(),
    'history clear': lambda lib_facade: lib_facade.clear_history(),

    # configuration API
    'workspace create': lambda lib_facade: lib_facade.create_workspace(),
    'workspace change': lambda lib_facade: lib_facade.change_workspace(),
    'workspace migrate': lambda lib_facade: lib_facade.migrate_workspace(),
    'workspace show': lambda lib_facade: lib_facade.show_workspace(),

    # postman API
    'postman parse': lambda lib_facade: lib_facade.parse_postman_coll(),
    'postman export': lambda lib_facade: lib_facade.export_to_postman_coll(),

    # cURL API
    'curl parse': lambda lib_facade: lib_facade.parse_curl_coll(),
    'curl export': lambda lib_facade: lib_facade.export_to_curl_scripts(),
}


def help():
    print('Help page')


def say_bay():
    print('Bye!')
