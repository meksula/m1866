exit = 'exit'
commands = {
    'exit': lambda: SayBay(),
    'add gunpowder': lambda: AddGunpowder(),
    'add shoot': lambda: AddShoot()
}


class Command:
    def execute(self):
        print('Method of `Command` object is not initialized!')


class AddShoot(Command):
    def execute(self):
        print('Shoot adding')


class AddGunpowder(Command):
    def execute(self):
        print('Gunpowder adding')


class SayBay(Command):
    def execute(self):
        print('Bye!')
