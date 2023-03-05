import pytest
import project  # on import will print something from __init__ file
from project.parsing.substituter import Substituter


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


def test_single_quotes():
    assert Substituter.substitute("'a'") == "a"
    assert Substituter.substitute("'a  b'") == "a  b"
    assert Substituter.substitute("'a | b'") == "a | b"


def test_double_quotes():
    assert Substituter.substitute('"a"') == "a"
    assert Substituter.substitute('"a  b"') == "a  b"
    assert Substituter.substitute('"a | b"') == "a | b"
