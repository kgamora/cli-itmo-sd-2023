from project.execution.executable import Executable
import argparse
import re
from os.path import isfile


class Grep(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)
        self.os_asked_help = False
        try:
            self.args = self._init_args()
        except SystemExit as se:
            if se.code == 0:
                self.os_asked_help = True
            else:
                raise se

    def _init_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-w", default=None)
        parser.add_argument("-A", default=0)
        parser.add_argument("-i", action="store_const", default=None, const=True)
        parser.add_argument("pattern", metavar="PATTERN", type=str)
        parser.add_argument("files", metavar="FILES", type=str, nargs="+")
        return parser.parse_args(self.arguments)

    def _init_pattern(self):
        pattern: str
        if self.args.w is not None:
            pattern = self._get_patten_for_word(self.args.w)
        else:
            pattern = self.args.pattern
        if self.args.i is not None:
            pattern = self._get_patten_for_case_insensitive(pattern)
        return pattern

    def _get_patten_for_word(self, word: str):
        return f"(\W|^){word}($|\W)"

    def _get_patten_for_case_insensitive(self, pattern: str):
        return f"{pattern}//i"

    def _find_by_regex(
            self, pattern: str, target_lines, additional_lines_number: int
    ) -> list[(str, (int, int))]:
        result, how_much_to_add = list(), list()

        for line in target_lines:

            for i, (match, (_, _)) in enumerate(result):
                if how_much_to_add[i]:
                    how_much_to_add[i] -= 1
                    match += line

            matches = re.search(pattern=pattern, string=line)
            if matches:
                left, right = matches.span()
                result.append((line, (left, right)))
                how_much_to_add.append(additional_lines_number)

        return result

    @Executable._may_throw
    def execute(self, stdin: str):
        """
        Executes the command and captures its output (stdout, stderr and return code).
        Behaves in the exact same manner as echo command in standard Linux distros but lacks its flags.
        :param stdin: command input stream
        :return: None
        """
        if self.os_asked_help:
            self.ret_code = 0
            return
        pattern = self._init_pattern()
        lines_number = self.args.A
        results = {}
        for file in self.args.files:
            if isfile(file):
                results[file] = self._find_by_regex(
                    pattern, Grep._get_file_text(file), lines_number
                )[0]
            else:
                self.stderr += file + " is not a valid file. \n"
        for key in sorted(results):
            text, (l, r) = results[key]
            self.stdout += ": ".join((key, text))

        self.ret_code = 0

    @staticmethod
    def _get_file_text(file_name: str):
        with open(file_name, "r") as content_file:
            yield content_file.readline()
