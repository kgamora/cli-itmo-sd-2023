import os
import pathlib
import pytest
import project
from project.application.context_manager import ContextManager  # on import will print something from __init__ file
from project.execution.commands.wc import *


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


def test_stdin():
    wc = WC()
    test_example = "Andhra Pradesh\nArunachal Pradesh\nAssam Bihar\nChhattisgarh"
    wc.execute(test_example)
    assert wc.stderr == ""
    assert wc.stdout == "      4       7      58"
    assert wc.ret_code == 0


def test_from_file():
    file_name = str(pathlib.Path(__file__).parent) + "/capitals.txt"
    wc = WC([file_name])
    capitals: list[str] = ["Hyderabad", "Itanagar", "Dispur", "Patna", "Raipur"]
    with open(file_name, "w+") as file:
        for capital in capitals:
            file.write(capital)
    wc.execute("")
    os.remove(file_name)
    assert wc.stderr == ""
    assert wc.stdout == f"     0     1    34 {file_name}"
    assert wc.ret_code == 0


def test_from_relative_file():
    test_dir = ContextManager().get_cwd() + os.path.sep + 'test/resources'
    ContextManager().set_cwd(test_dir)
    file_name = test_dir + os.path.sep + "capitals.txt"
    capitals: list[str] = ["Hyderabad", "Itanagar", "Dispur", "Patna", "Raipur"]
    with open(file_name, "w+") as file:
        for capital in capitals:
            file.write(capital)
            
    wc = WC(["capitals.txt"])
    wc.execute("")
    ContextManager()._clear()
    os.remove(file_name)
    assert wc.stderr == ""
    assert wc.stdout == f"     0     1    34 capitals.txt"
    assert wc.ret_code == 0
