import unittest

from m1866_lib.cli.interact import UserInteractor


class TestInteract(unittest.TestCase):

    def test_should_has_init_value_as_False(self):
        interactor = UserInteractor()
        self.assertFalse(interactor.get_last())

    def test_should_correctly_change_t_f_input_value(self):
        interactor = UserInteractor('n')
        self.assertFalse(interactor.get_last())

    def test_should_correctly_change_t_f_input_value_as_true(self):
        interactor = UserInteractor('y')
        self.assertTrue(interactor.get_last())
