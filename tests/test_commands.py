import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import os
import unittest
from unittest.mock import MagicMock
from commands import ls, cd, chown, history
from emulator import ShellEmulator

class ShellGUI:
    def __init__(self):
        pass
    def display_output(self, *args):
        pass
class TestShellCommands(unittest.TestCase):
    
    def setUp(self):

        self.fs = MagicMock()
        self.shell_gui = ShellGUI()
        self.shell = ShellEmulator(username='user1', tar_path='vfs.tar', log_path='test.log')
        self.shell.fs = self.fs
        self.shell.current_dir = '/home/user' 

        self.fs.list_dir.return_value = ['file1.txt', 'file2.txt']
        self.fs.change_dir.side_effect = lambda current, new: new if new in ['/home/user', '/home'] else FileNotFoundError
        self.fs.change_owner.return_value = None  

    def test_ls_command(self):
        output = ls.ls(self.fs, self.shell_gui, self.shell.current_dir, "/")
        self.fs.list_dir.assert_called_with(self.shell.current_dir)
        self.assertIsNone(output) 

    def test_cd_command_success(self):
        new_dir = '/home'
        cd.cd(self.fs, self.shell_gui, self.shell, [new_dir])
        self.assertEqual("/home", new_dir) 

    def test_cd_command_failure(self):
        self.fs.change_dir.side_effect = FileNotFoundError
        dir =cd.cd(self.fs, self.shell_gui, self.shell, ['/non_existing_directory'])
        self.assertEqual(dir, None)

    def test_chown_command_success(self):
        chown.chown(self.fs, self.shell_gui, self.shell, ['user1', 'file1.txt'])
        self.fs.change_owner.assert_called_with('/home/user/file1.txt', 'user1')

    def test_chown_command_failure(self):
        result = chown.chown(self.fs, self.shell_gui, self.shell, ['user1', 'non_existing_file.txt'])
        self.assertEqual(result, None)

    def test_history_command(self):
        self.shell.history.append('ls')
        self.shell.history.append('cd /home')
        output = history.history(self.shell_gui, self.shell)
        self.assertEqual(len(self.shell.history), 2)

if __name__ == '__main__':
    unittest.main()