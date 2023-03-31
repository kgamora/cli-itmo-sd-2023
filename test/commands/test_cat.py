import os
from typing import ContextManager

import pytest

from project.execution.commands.cat import Cat
from project.application.context_manager import ContextManager
from project.utils.fileutils import convert_to_abspath


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


FILE_NAME = "capital.txt"
FILE_NAME_NOT_EXISTS = ""
str_test: str = "Hyderabad Itanagar Dispur Patna Raipur"


def create_file(file_name):
    with open(file_name, "w+") as file:
        file.write(str_test)


def remove_file(file_name):
    os.remove(file_name)


def test_stdin():
    stdin = "Hello, world"
    cat = Cat()
    cat.execute(stdin)
    assert stdin == cat.stdout


def test_with_relative_path():
    test_dir = ContextManager().get_cwd() + os.path.sep + "test_dir"
    file = test_dir + os.path.sep + FILE_NAME
    os.mkdir(test_dir)
    create_file(file)

    ContextManager().set_cwd(test_dir)
    cat = Cat([FILE_NAME])
    cat.execute()
    ContextManager()._clear()

    remove_file(file)
    os.rmdir(test_dir)

    print(cat.stdout)
    assert str_test == cat.stdout


def test_file_exists():
    create_file(FILE_NAME)
    cat = Cat([FILE_NAME])
    cat.execute()
    remove_file(FILE_NAME)
    print(cat.stdout)
    assert str_test == cat.stdout


def test_file_not_exists():
    cat = Cat([FILE_NAME_NOT_EXISTS])
    cat.execute("")
    assert cat.stderr != ""
