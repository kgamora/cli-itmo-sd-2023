import pytest
import project  # on import will print something from __init__ file
from project.execution.commands.global_executable import GlobalExecutor


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


def test_poweroff():
    assert True
    GlobalExecutor(["poweroff"]).execute()
    assert False
