import pytest
import project  # on import will print something from __init__ file
from project.execution.commands.echo import Echo


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


def test_basic():
    text_to_ignore = "This text should be ignored"
    text_to_return = "This text should be returned"
    echo = Echo(text_to_return.split())
    echo.execute()
    assert echo.stdout != text_to_ignore
    assert echo.stdout == text_to_return


def test_empty():
    empty_echo = Echo([])
    empty_echo.execute()
    assert not empty_echo.stdout
