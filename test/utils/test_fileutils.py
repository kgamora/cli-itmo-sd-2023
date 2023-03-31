import pytest
import project  # on import will print something from __init__ file
from project.application.context_manager import ContextManager
from project.utils.fileutils import convert_to_abspath
import os

abspath = os.path.abspath("/")
sep = os.path.sep

def setup_module(module):
    print("basic setup module")
    ContextManager().set_cwd(abspath + "test" + sep + "dir")


def teardown_module(module):
    print("teardown module")
    ContextManager()._clear()


def test_relative_double_dots():
    assert abspath + "test" == convert_to_abspath("..")


def test_relative_one_dot():
    assert abspath + "test" + sep + "dir" == convert_to_abspath(".")


def test_relative_one_dir():
    assert abspath + "test" + sep + "dir" + sep + "down" == convert_to_abspath("down")


def test_absolute():
    assert abspath + "absolute" == convert_to_abspath(abspath + "absolute")


def test_relative_to_home():
    assert os.path.expanduser("~") + sep + "dir" == convert_to_abspath("~" + sep + "dir")


def test_absolute_with_double_dots():
    assert abspath + "absolute" == convert_to_abspath(abspath + "absolute" + sep + "dir" + sep + "..")


def test_absolute_with_dot():
    assert abspath + "absolute" + sep + "dir" == convert_to_abspath(abspath + "absolute" + sep + "dir" + sep + ".")
