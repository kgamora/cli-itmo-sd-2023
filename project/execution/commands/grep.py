from project.execution.executable import Executable
from project.parsing.custom_arg_parser import CustomArgumentParser
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
        except CustomArgumentParser.ArgumentException as ex:
            self.stderr += str(ex) + "\n"
            self.ret_code = 2

    def _init_args(self):
        parser = CustomArgumentParser()
        parser.add_argument(
            "-w", action="store_const", default=None, const=True, help="searching words"
        )
        parser.add_argument(
            "-A", default=0, type=int, help="how much lines show after matching"
        )
        parser.add_argument(
            "-i", action="store_const", default=None, const=True, help="ignore case"
        )
        parser.add_argument(
            "pattern", metavar="PATTERN", type=str, help="pattern to searching"
        )
        parser.add_argument(
            "files",
            metavar="FILES",
            type=str,
            nargs="+",
            help="list of files to search at",
        )
        parser.prog = "grep"
        return parser.parse_args(self.arguments)

    def _init_pattern(self):
        pattern: str
        if self.args.w:
            pattern = self._get_patten_for_word(self.args.pattern)
        else:
            pattern = self.args.pattern
        if self.args.i:
            pattern = self._get_patten_for_case_insensitive(pattern)
        return pattern

    @staticmethod
    def _get_patten_for_word(word: str):
        return rf"(\W|^){word}($|\W)"

    @staticmethod
    def _get_patten_for_case_insensitive(pattern: str):
        return rf"(?i){pattern}"

    @staticmethod
    def _find_by_regex(
        pattern: str, target_lines, additional_lines_number: int
    ) -> list[(str, (int, int))]:
        result = list()
        current_accept = 0

        for line in target_lines:
            matches = re.search(pattern=pattern, string=line)
            if matches:
                current_accept = additional_lines_number
                left, right = matches.span()
                result.append((line, (left, right)))
            elif current_accept > 0:
                result.append((line, (0, 0)))
                current_accept -= 1
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
        if self.ret_code and self.ret_code > 0:
            return

        pattern = self._init_pattern()
        lines_number = self.args.A
        results = {}
        for file in self.args.files:
            if isfile(file):
                results[file] = self._find_by_regex(
                    pattern, Grep._get_file_text(file), lines_number
                )
            else:
                self.stderr += "grep" + f" {file}: Это каталог\n"
        for file in sorted(results):
            for text, (_, _) in results[file]:
                self.stdout += ": ".join((file, text))

        self.ret_code = 0

    @staticmethod
    def _get_file_text(file_name: str):
        with open(file_name, "r") as content_file:
            for line in content_file:
                yield line
        return
