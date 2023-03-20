import os

from project.execution.commands.grep import Grep


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


FILE_NAME = "capital.txt"
str_test: str = """Hyderabad Itanagar
Dispur Patna Raipur, itanagar
Random Text Hello World"""


def create_file():
    with open(FILE_NAME, "w+") as file:
        file.write(str_test)


def remove_file():
    os.remove(FILE_NAME)


def test_easy_pattern():
    create_file()
    grep = Grep(["a", f"./{FILE_NAME}"])
    grep.execute(None)
    remove_file()
    str_answer: str = """./capital.txt: Hyderabad Itanagar
./capital.txt: Dispur Patna Raipur, itanagar
./capital.txt: Random Text Hello World"""
    assert str_answer == grep.stdout


def test_search_word():
    create_file()
    grep = Grep(["-w", "Hyderabad", f"./{FILE_NAME}"])
    grep.execute(None)
    remove_file()
    str_answer = "./capital.txt: Hyderabad Itanagar\n"
    assert str_answer == grep.stdout


def test_flag_i_word():
    create_file()
    grep = Grep(["-w", "itanagar", "-i", f"./{FILE_NAME}"])
    grep.execute(None)
    remove_file()
    str_answer = """./capital.txt: Hyderabad Itanagar
./capital.txt: Dispur Patna Raipur, itanagar
"""
    assert str_answer == grep.stdout


def test_flag_a_word():
    create_file()
    grep = Grep(["-w", "Itanagar", "-i", "-A", "1", f"./{FILE_NAME}"])
    grep.execute(None)
    remove_file()
    str_answer = """./capital.txt: Hyderabad Itanagar
./capital.txt: Dispur Patna Raipur, itanagar
./capital.txt: Random Text Hello World"""
    assert str_answer == grep.stdout
