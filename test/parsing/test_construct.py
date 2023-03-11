import pytest
import project  # on import will print something from __init__ file
from project.execution.commands.cat import Cat
from project.execution.commands.pwd import PWD
from project.parsing.constructor import Constructor


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


def test_construct_pwd():
    constructor = Constructor()
    assert constructor.construct(["pwd"]).__class__ == PWD
    assert constructor.construct(["pwd", "a", "b"]).__class__ == PWD


def test_construct_cat():
    constructor = Constructor()
    my_cat = constructor.construct(["cat", "text.txt"])
    assert my_cat.__class__ == Cat
    assert my_cat.arguments == ["text.txt"]
    assert constructor.construct(["cat", "text1.txt", "text2.txt"]).arguments == [
        "text1.txt",
        "text2.txt",
    ]
