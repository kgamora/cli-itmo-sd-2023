import pytest
import project  # on import will print something from __init__ file
from project.execution.commands.assign import Assign
from project.application.context_manager import ContextManager


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("teardown module")


def test_throws():
    ignore = "this text should be ignored"
    with pytest.raises(IndexError):
        Assign(["not_enough_args"]).execute(ignore)


def test_basic():
    ContextManager()._clear()
    var, val = "var", "val"
    assert not ContextManager().get_var(var)
    assign = Assign([var, val])
    assign.execute("")
    assert ContextManager().get_var(var) == val
    assert not assign.stdout
    ContextManager()._clear()


def test_string_assign():
    ContextManager()._clear()
    var, val = "var", "'sdf|fds'"
    assert not ContextManager().get_var(var)
    assign = Assign([var, val])
    assign.execute("")
    assert ContextManager().get_var(var) == val
    assert not assign.stdout
    ContextManager()._clear()
