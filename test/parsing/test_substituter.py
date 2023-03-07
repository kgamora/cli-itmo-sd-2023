from project.application.context_manager import ContextManager
from project.parsing.substituter import Substituter


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


context = ContextManager()


def test_easy():
    context.set_var("name", "world")
    context.set_var("x", "3")
    context.set_var("y", "4")
    assert "Hello, world" == Substituter.substitute("Hello, $name")
    assert "3+4=7" == Substituter.substitute("$x+$y=7")
    assert "$name $x$y" == Substituter.substitute("world 34")


def test_not_exists_substitution():
    assert "" == Substituter.substitute("name_world")
    assert "" == Substituter.substitute("x")
    assert "" == Substituter.substitute("y")


def test_hard():
    context.set_var("name", "world")
    context.set_var("key", "$name")

    assert "world" == Substituter.substitute("$key")
