import pytest
import project  # on import will print something from __init__ file
from project.execution.commands.exit import Exit


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("teardown module")


def test_exit():
    with pytest.raises(SystemExit):
        Exit().execute("")
