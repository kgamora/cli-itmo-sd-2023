import os

from project.execution.commands.cat import Cat


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


FILE_NAME = "capital.txt"
FILE_NAME_NOT_EXISTS = ""
str_test: str = "Hyderabad Itanagar Dispur Patna Raipur"


def create_file():
    with open(FILE_NAME, "w+") as file:
        file.write(str_test)


def remove_file():
    os.remove(FILE_NAME)


def test_stdin():
    stdin = "Hello, world"
    cat = Cat()
    cat.execute(stdin)
    assert stdin == cat.stdout


def test_file_exists():
    create_file()
    cat = Cat([FILE_NAME])
    cat.execute()
    remove_file()
    print(cat.stdout)
    assert str_test == cat.stdout


def test_file_not_exists():
    cat = Cat([FILE_NAME_NOT_EXISTS])
    cat.execute("")
    assert cat.stderr is not None
