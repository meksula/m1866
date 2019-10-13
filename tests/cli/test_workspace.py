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
        wsp_dir = Workspace("default").instance.workspace_pointer()
        print(wsp_dir)
        subprocess.check_call('ls ' + wsp_dir, shell=True)
