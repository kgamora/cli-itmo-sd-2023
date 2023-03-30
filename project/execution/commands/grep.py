from project.execution.executable import Executable
from project.parsing.custom_arg_parser import CustomArgumentParser
import re
from os.path import isfile

from project.utils.fileutils import convert_to_abspath


class Grep(Executable):
    class GrepException(Exception):
        pass

    _parser = CustomArgumentParser()
    _parser.add_argument(
        "-w", action="store_const", default=None, const=True, help="searching words"
    )
    _parser.add_argument(
        "-A", default=0, type=int, help="how much lines show after matching"
    )
    _parser.add_argument(
        "-i", action="store_const", default=None, const=True, help="ignore case"
    )
    _parser.add_argument(
        "pattern", metavar="PATTERN", type=str, help="pattern to searching"
    )
    _parser.add_argument(
        "files",
        metavar="FILES",
        type=str,
        nargs="+",
        help="list of files to search at",
    )
    _parser.prog = "grep"
    _parser.description = """grep  searches  for  PATTERNS  in  each  FILE.  PATTERNS is one or more
            patterns separated by newline characters, and  grep  prints  each  line
            that  matches a pattern.
            Typically, PATTERNS should be quoted when grep is used in a shell command."""

    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)
        self.os_asked_help = False
        try:
            self.args = self._parser.parse_args(self.arguments)
        except SystemExit as se:
            self.ret_code = se.code
        except CustomArgumentParser.ArgumentException as ex:
            self.stderr += str(ex) + "\n"
            self.ret_code = 2

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

        try:
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
        except re.error as err:
            raise Grep.GrepException(
                f"{err.lineno}:{err.colno} Error of pattern matching: {err.msg}: '{err.pattern}'."
            )
        except BaseException:
            raise Grep.GrepException("Error due pattern matching was occurred.")

    @Executable._may_throw
    def execute(self, stdin: str):
        """
        grep  searches  for  PATTERNS  in  each  FILE.  PATTERNS is one or more
        patterns separated by newline characters, and  grep  prints  each  line
        that  matches a pattern.
        Typically, PATTERNS should be quoted when grep is used in a shell command.
        :param stdin: command input stream is ignored
        :return: None
        """
        if self.ret_code is not None:
            return

        pattern = self._init_pattern()
        lines_number = self.args.A
        results = {}
        for file in self.args.files:
            abs_file = convert_to_abspath(file)
            if isfile(abs_file):
                results[file] = self._find_by_regex(
                    pattern, Grep._get_file_text(abs_file), lines_number
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
