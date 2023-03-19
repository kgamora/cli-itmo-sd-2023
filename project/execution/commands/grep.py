from project.execution.executable import Executable
import argparse
from os.path import isfile


class Grep(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)
        self.args = self._init_args()

    def _init_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-w', default=None)
        parser.add_argument('-A', default=0)
        parser.add_argument('-i', action='store_const', default=None, const=True)
        parser.add_argument('tail', metavar='N', type=str, nargs='+')
        return parser.parse_args(self.arguments)

    def _init_pattern(self):
        pattern = ""
        if self.args.w is not None:
            pattern = self._get_patten_for_word(self.args.w)
        else:
            pattern = self.args.tail[0]
            self.args.tail = self.args.tail[1:]
        if self.args.i is not None:
            pattern = self._get_patten_for_case_insensitive(pattern)
        return pattern

    def _get_patten_for_word(self, word: str):
        return f'(\W|^){word}($|\W)'

    def _get_patten_for_case_insensitive(self, pattern: str):
        return f'{pattern}//i'

    def _find_by_regex(self, pattern: str, text: str, additional_lines_number: int):
        pass

    @Executable._may_throw
    def execute(self, stdin: str):
        """
        Executes the command and captures its output (stdout, stderr and return code).
        Behaves in the exact same manner as echo command in standard Linux distros but lacks its flags.
        :param stdin: command input stream
        :return: None
        """
        pattern = self._init_pattern()
        lines_number = self.arg.A
        for file in self.args.tail:
            if isfile(file):
                content = Grep._get_file_text(file)
                self._find_by_regex(pattern, content, lines_number)

        self.stdout = " ".join(self.arguments)
        self.ret_code = 0

    def _get_func(self, name):
        return

    @staticmethod
    def _get_file_text(file_name):
        with open(file_name, 'r') as content_file:
            content = content_file.read()
        return content
