import pytest
import project  # on import will print something from __init__ file
from project.application.context_manager import ContextManager
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


def test_easy():
    ContextManager().set_var("name", "world")
    ContextManager().set_var("x", "3")
    ContextManager().set_var("y", "4")
    assert "Hello, world" == Substituter.substitute("Hello, $name")
    assert "3+4=7" == Substituter.substitute("$x+$y=7")
    assert "world 34" == Substituter.substitute("$name $x$y")
    ContextManager()._clear()


def test_not_exists_substitution():
    assert "" == Substituter.substitute("$name_world")
    assert "" == Substituter.substitute("$x")
    assert "" == Substituter.substitute("$y")
