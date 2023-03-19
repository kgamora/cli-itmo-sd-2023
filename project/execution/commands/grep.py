from project.execution.executable import Executable
import argparse
from os.path import isfile


class Grep(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)
        self.args = self._init_args()

    def _init_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-w', default=False)
        parser.add_argument('-A', default=False)
        parser.add_argument('-i', action='store_const', default=False, const=True)
        parser.add_argument('files', metavar='N', type=str, nargs='+')
        return parser.parse_args(self.arguments)

    def _find_by_regex(self, pattern:str, text:str, additional_lines_number:int):
        pass

    @Executable._may_throw
    def execute(self, stdin: str):
        """
        Executes the command and captures its output (stdout, stderr and return code).
        Behaves in the exact same manner as echo command in standard Linux distros but lacks its flags.
        :param stdin: command input stream
        :return: None
        """
        for file in self.args.files:
            if isfile(file):
                content = Grep._get_file_text(file)
                print(content)

        self.stdout = " ".join(self.arguments)
        self.ret_code = 0

    @staticmethod
    def _get_file_text(file_name):
        with open(file_name, 'r') as content_file:
            content = content_file.read()
        return content


test = Grep(["-w", "word", "grep.py", "exit.py", "file", "file"])

test.execute(None)
