import os
import pathlib
import sys

from project.application.application import Application


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


FILE_IN = str(pathlib.Path(__file__).parent) + "/test_in.txt"
FILE_OUT = str(pathlib.Path(__file__).parent) + "/test_out.txt"
TEST_TEXT_IN = ["echo 'hello world' | cat\n", "echo 'alone' | cat\n"]
TEST_TEXT_OUT = ["hello world\n", "alone\n"]


def init_files(input_list: list[str] = TEST_TEXT_IN):
    i = open(FILE_IN, "w")
    i.write("".join(input_list))
    i.write("exit")


def delete_files():
    os.remove(FILE_IN)
    os.remove(FILE_OUT)


class ModuleTest:
    def __init__(self, input_str=None):
        self.out = None
        self.i = None
        self.tmp_out = None
        self.tmp_in = None
        self.app = Application()
        if input_str:
            init_files(input_str)
        else:
            init_files()

    def change_streams(self):
        self.tmp_in = sys.stdin
        self.tmp_out = sys.stdout
        self.i = open(FILE_IN, "r")
        self.out = open(FILE_OUT, "w")
        sys.stdin = self.i
        sys.stdout = self.out

    def run(self):
        try:
            self.app.run()
        except BaseException:
            ...

    def return_streams(self):
        sys.stdin = self.tmp_in
        sys.stdout = self.tmp_out
        self.i.close()
        self.out.close()

    def __del__(self):
        delete_files()


def test_easy():
    test = ModuleTest()
    test.change_streams()
    test.run()
    test.return_streams()
    with open(FILE_OUT) as f:
        for out_app, out in zip(f.readlines(), TEST_TEXT_OUT):
            assert out_app == out


def test_some_inputs():
    test = ModuleTest(
        [
            "var='sdf|fds'\n",
            "echo $var\n",
        ]
    )
    test.change_streams()
    test.run()
    test.return_streams()
    with open(FILE_OUT) as f:
        for out_app, out in zip(
            f.readlines(),
            [
                "sdf|fds\n",
            ],
        ):
            assert out_app == out


def test_empty():
    test = ModuleTest(
        [
            "echo 'fff' | echo\n",
        ]
    )
    test.change_streams()
    test.run()
    test.return_streams()
    with open(FILE_OUT) as f:
        for out_app, out in zip(f.readlines(), [""]):
            assert out_app == out


def test_empty():
    test = ModuleTest(
        [
            "echo 'fff' | echo\n",
        ]
    )
    test.change_streams()
    test.run()
    test.return_streams()
    with open(FILE_OUT) as f:
        for out_app, out in zip(f.readlines(), [""]):
            assert out_app == out


def test_empty():
    test = ModuleTest(
        [
            "echo 'fff' | cat | cat | cat | cat | cat | cat | cat | cat | cat | cat | cat\n"
        ]
    )
    test.change_streams()
    test.run()
    test.return_streams()
    with open(FILE_OUT) as f:
        for out_app, out in zip(f.readlines(), ["fff\n"]):
            assert out_app == out


def test_without_space():
    test = ModuleTest(["echo 'F'|cat\n"])
    test.change_streams()
    test.run()
    test.return_streams()
    with open(FILE_OUT) as f:
        for out_app, out in zip(f.readlines(), ["F\n"]):
            assert out_app == out
