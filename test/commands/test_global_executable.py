import os

import pytest
import project
from project.application.context_manager import (
    ContextManager,
)  # on import will print something from __init__ file
from project.execution.commands.global_executable import GlobalExecutor


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


# def test_poweroff():
#     assert True
#     GlobalExecutor(["poweroff"]).execute()
#     assert True


def test_ls():
    ge = GlobalExecutor(["ls", "-al"])
    ge.execute()
    filename = os.path.basename(__file__)
    print(filename)
    print(ge.stdout)
    assert ge.stdout.__contains__(filename) or ge.stdout.__contains__("README.md")


def test_ls():
    test_dir = ContextManager().get_cwd() + os.path.sep + "test/resources/test_ls"
    ContextManager().set_cwd(test_dir)
    ge = GlobalExecutor(["ls", "-al"])
    ge.execute()
    ContextManager()._clear()
    print(ge.stdout)
    assert ge.stdout.__contains__("test_ls_file")
