import os

import pytest
import project  # on import will print something from __init__ file
from project.execution.commands.wc import *


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


def test_stdin():
    wc = WC()
    test_example = "Andhra Pradesh\nArunachal Pradesh\nAssam Bihar\nChhattisgarh"
    wc.execute(test_example)
    assert wc.stderr is None
    assert wc.stdout == "5  7 58"
    assert wc.ret_code == 0


def test_from_file():
    wc = WC(["capitals.txt"])
    capitals: list[str] = ["Hyderabad", "Itanagar", "Dispur", "Patna", "Raipur"]
    with open("capital.txt", "w+") as file:
        for capital in capitals:
            file.write(capital)
    wc.execute("")
    os.remove("capital.txt")
    assert wc.stderr is None
    assert wc.stdout == "5  5 39 capital.txt"
    assert wc.ret_code == 0
