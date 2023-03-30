import pytest
import project  # on import will print something from __init__ file
from project.application.context_manager import ContextManager
from project.utils.fileutils import convert_to_abspath
import os


def setup_module(module):
    print("basic setup module")
    ContextManager().set_cwd("/test/dir")


def teardown_module(module):
    print("teardown module")
    ContextManager()._clear()


def test_relative_double_dots():
    assert "/test" == convert_to_abspath("..")


def test_relative_one_dot():
    assert "/test/dir" == convert_to_abspath(".")


def test_relative_one_dir():
    assert "/test/dir/down" == convert_to_abspath("down")


def test_absolute():
    assert "/absolute" == convert_to_abspath("/absolute")


def test_relative_to_home():
    assert os.path.expanduser("~") + "/dir" == convert_to_abspath("~/dir")


def test_absolute_with_double_dots():
    assert "/absolute" == convert_to_abspath("/absolute/dir/..")


def test_absolute_with_dot():
    assert "/absolute/dir" == convert_to_abspath("/absolute/dir/.")
