from project.execution.commands.pwd import *


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


def test_1():
    pwd = PWD()
    pwd.execute("")
    assert os.getcwd() == pwd.stdout
    assert pwd.ret_code == 0
