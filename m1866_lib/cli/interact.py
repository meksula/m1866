from colorama import Style, Fore


class UserInteractor:
    instance = None

    def __init__(self, user_input=False):
        if not UserInteractor.instance:
            UserInteractor.instance = UserInteractor.__UserIntercator(user_input)
        else:
            if str(user_input) is 'last':
                return
            else:
                self.instance.est_interact(user_input)

    def get_last(self):
        return self.instance.t_f_input

    class __UserIntercator:
        t_f_input = False

        def __init__(self, user_input):
            self.t_f_input = self.est_interact(user_input)

        def est_interact(self, user_input):
            interaction = {
                'y': True,
                'n': False
            }
            try:
                self.t_f_input = interaction[str(user_input).lower()]
                return self.t_f_input
            except KeyError:
                print(Fore.RED, 'Invalid input. Available only `y` or `n`', Style.RESET_ALL)
