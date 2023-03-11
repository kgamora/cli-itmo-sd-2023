import pytest
import project  # on import will print something from __init__ file
from project.parsing.lexer import Lexer


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


def test_1():
    assert Lexer.lex("") == []
    assert Lexer.lex("pwd") == ["pwd"]
    assert Lexer.lex('echo "cat"') == ["echo", '"cat"']
    assert Lexer.lex('echo "|cat"') == ["echo", '"|cat"']


def test_2():
    assert Lexer.lex('echo | "cat"') == ["echo", "|", '"cat"']
    assert Lexer.lex("echo ; 'cat'") == ["echo", ";", "'cat'"]
    assert Lexer.lex("echo = 'cat'") == ["echo", "=", "'cat'"]
    assert Lexer.lex("echo=cat") == ["echo", "=", "cat"]
