import os

import pytest
from project.application.context_manager import ContextManager
from project.execution.commands.cd import CD


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


@pytest.fixture(autouse=True)
def setup():
    # Set up code here
    print("Running setup before each test")
    ContextManager().set_cwd(
        ContextManager().get_cwd() + os.path.sep + "test/resources/test_cd"
    )
    yield
    ContextManager()._clear()


def test_one_dir():
    prev = ContextManager().get_cwd()
    cd = CD(["a"])
    cd.execute("")
    assert prev + os.path.sep + "a" == ContextManager().get_cwd()
    assert cd.stderr == ""
    assert cd.ret_code == 0


def test_two_dir():
    prev = ContextManager().get_cwd()
    cd = CD(["a" + os.path.sep + "b"])
    cd.execute("")
    assert prev + os.path.sep + "a" + os.path.sep + "b" == ContextManager().get_cwd()
    assert cd.stderr == ""
    assert cd.ret_code == 0


def test_two_dots():
    prev = ContextManager().get_cwd()
    ContextManager().set_cwd(ContextManager().get_cwd() + os.path.sep + "a")
    cd = CD([".."])
    cd.execute("")
    assert prev == ContextManager().get_cwd()
    assert cd.stderr == ""
    assert cd.ret_code == 0


def test_one_dot():
    prev = ContextManager().get_cwd()
    cd = CD(["."])
    cd.execute("")
    assert prev == ContextManager().get_cwd()
    assert cd.stderr == ""
    assert cd.ret_code == 0


def test_not_exist():
    prev = ContextManager().get_cwd()
    cd = CD(["not_exist"])
    cd.execute("")
    assert cd.stderr != ""
    assert cd.ret_code != 0


def test_not_dir():
    prev = ContextManager().get_cwd()
    cd = CD(["a/b/c/file"])
    cd.execute("")
    assert cd.stderr != ""
    assert cd.ret_code != 0


def test_no_params():
    cd = CD()
    cd.execute("")
    assert os.path.expanduser("~") == ContextManager().get_cwd()
    assert cd.ret_code == 0
