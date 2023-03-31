import pytest
import project  # on import will print something from __init__ file
from project.execution.commands.ls import LS
from project.application.context_manager import ContextManager
from project.utils.fileutils import convert_to_abspath
from os.path import sep as os_sep
from os import makedirs, removedirs

def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("teardown module")

def get_local_dir_name(name:str) -> str:
     return "test" + os_sep + "commands" +  os_sep + name

def test_simple():
    ls = LS()
    ls.execute()
    assert ls.ret_code == 0
    assert len(ls.stdout) > 0 

def test_empty_cur_dir():
    dir_name = get_local_dir_name("ls_test_dirs")
    makedirs(dir_name)
    cm = ContextManager()
    cm.set_cwd(convert_to_abspath(dir_name))
    ls = LS()
    ls.execute()
    removedirs(dir_name)
    cm._clear()

    assert ls.ret_code == 0
    assert ls.stdout == ''
    assert ls.stderr == ''

        
def test_dir_with_dirs():
    dir_name = get_local_dir_name("ls_test_dirs")
    makedirs(dir_name)
    cm = ContextManager()
    cm.set_cwd(convert_to_abspath(dir_name))
    subdirs = [str(i) for i in range(10)]
    all_dirs = ""
    for d in subdirs:
        makedirs(dir_name + os_sep + d)
        if(len(all_dirs) != 0):
            all_dirs += " "
        all_dirs += d + os_sep

    ls = LS()
    ls.execute()
    for d in subdirs:
        removedirs(dir_name + os_sep + d)
    cm._clear()

    assert ls.ret_code == 0
    assert ls.stderr == ''
    assert ls.stdout == all_dirs