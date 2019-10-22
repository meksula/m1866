import subprocess
import unittest

from m1866_lib.cli.workspace import Workspace


class TestWorkspace(unittest.TestCase):

    def test_check_if_singleton_work_correctly(self):
        workspace_name = "some_name"
        wsp = Workspace("default")
        wsp_next = Workspace(workspace_name)

        self.assertIsNotNone(wsp)
        self.assertIsNotNone(wsp.instance)
        self.assertEqual(wsp.instance.show_workspace(), wsp_next.instance.show_workspace())
        self.assertEqual(wsp_next.instance.show_workspace(), workspace_name)
        self.assertEqual(wsp.instance.show_workspace(), workspace_name)

    def test_workspace_pointer_should_point_correct_dir(self):
        workspace = Workspace("default")
        wsp_dir = workspace.instance.workspace_pointer()

        whomai = str(subprocess.check_output('whoami', shell=True))

        expected_dir = '/home/' + whomai[2:-3] + '/.m1866/workspaces/default'
        self.assertEqual(expected_dir, wsp_dir)

    def test_workspace_is_workspace_establish_should_return_true(self):
        workspace = Workspace("default")
        result = workspace.is_workspace_established()

        self.assertTrue(result)

    def test_workspace_is_workspace_establish_should_return_false(self):
        workspace = Workspace(None)
        result = workspace.is_workspace_established()

        self.assertFalse(result)
