import pytest
import project  # on import will print something from __init__ file
from project.execution.commands.exit import Exit


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("test passed")


def test_exit():
    with pytest.raises(SystemExit):
        Exit().execute("")
