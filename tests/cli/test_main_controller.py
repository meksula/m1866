import unittest
from unittest.mock import Mock

from m1866_lib.cli.main_controller import MainFlowController


class TestMainController(unittest.TestCase):
    command = 'run'
    command_with_options = 'run -> timeout=500 method=PUT headers=43'
    command_without_options = 'run ->'
    command_with_alone_options = 'run -> save silent no-print'

    def prepare(self):
        mock_a = Mock()
        mock_b = Mock()
        return MainFlowController(mock_a, mock_b)

    # args_extract
    def test_should_return_command_without_options(self):
        sut = self.prepare()
        result = sut.args_extract(self.command)

        self.assertEqual(result[0], self.command)
        self.assertTrue(len(str(result[1])) == 0)

    # args_extract
    def test_should_return_command_with_correct_amount_of_options(self):
        sut = self.prepare()
        result = sut.args_extract(self.command_with_options)
        command = result[0]
        options = result[1]

        self.assertEqual(self.command, command)
        self.assertEqual(3, len(options))

        self.assertEqual(options[0][0], 'timeout')
        self.assertEqual(options[0][1], '500')

        self.assertEqual(options[1][0], 'method')
        self.assertEqual(options[1][1], 'PUT')

        self.assertEqual(options[2][0], 'headers')
        self.assertEqual(options[2][1], '43')

    # args_extract
    def test_should_correctly_divide_command(self):
        sut = self.prepare()
        result = sut.args_extract(self.command_without_options)
        command = result[0]
        options = result[1]

        self.assertEqual(self.command, command)
        self.assertEqual(0, len(options))

    def test_should_correctly_divide_command_with_name_without_value(self):
        sut = self.prepare()
        result = sut.args_extract(self.command_with_alone_options)
        command = result[0]
        options = result[1]

        self.assertEqual(self.command, command)
        self.assertEqual(3, len(options))

        self.assertEqual('save', options[0][0])
        self.assertEqual('silent', options[1][0])
        self.assertEqual('no-print', options[2][0])

        self.assertEqual(0, len(options[0][1]))
        self.assertEqual(0, len(options[1][1]))
        self.assertEqual(0, len(options[2][1]))
