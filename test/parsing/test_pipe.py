import sys, os, pathlib

from project.application.application import Application


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


FILE_IN = str(pathlib.Path(__file__).parent) + "/test_in.txt"
FILE_OUT = str(pathlib.Path(__file__).parent) + "/test_out.txt"
TEST_TEXT_IN = "echo 'hello world' | cat\n"
TEST_TEXT_OUT = "hello world"


def init_files():
    i = open(FILE_IN, "w")
    i.write(TEST_TEXT_IN)
    i.write("exit")
    out = open(FILE_OUT, "w")
    out.write(TEST_TEXT_OUT)


def delete_files():
    os.remove(FILE_IN)
    os.remove(FILE_OUT)


class ModuleTest:
    def __init__(self):
        self.app = Application()
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
        for i in f.readlines():
            assert i == TEST_TEXT_OUT + "\n"
