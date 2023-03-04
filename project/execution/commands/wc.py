import os

from project.execution.executable import Executable


class WC(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)
        self.max_len = 0
        self.total_line = 0
        self.total_word = 0
        self.total_byte = 0
        if not self.arguments:
            self.arguments = []

    # @Executable._may_throw
    def execute(self, stdin: str = ""):
        """
        Executes the command and captures its output (stdout, stderr and return code).
        Behaves in the exact same manner as wc command in standard Linux distros but lacks its flags.
        :param stdin: command input stream
        :return: None
        """
        self.stdout = ""
        self.__print_if(stdin and len(stdin) != 0, stdin)
        output, offset = self.__get_info()
        template = (
            "{:" + offset + "d}{:" + offset + "d}{:" + offset + "d} {:" + offset + "s}"
        )
        for out in output:
            if "dir" in out:
                self.stdout += out["dir"] + "\n"
            if "file" in out:
                self.stdout += template.format(*out["file"]) + "\n"
        if len(self.arguments) != 0:
            self.stdout += template.format(
                self.total_line, self.total_word, self.total_byte, "итого"
            )
        self.ret_code = 0

    def __get_info(self):
        output = []
        for argument in self.arguments:
            if self.__is_file(argument):
                count_new_line, count_words, size = self.__get_info_about_file(argument)
                self.total_line += count_new_line
                self.total_word += count_words
                self.total_byte += size
                max_len = max(self.max_len, len(str(self.total_byte)))
                output.append({"file": (count_new_line, count_words, size, argument)})
            elif self.__is_dir(argument):
                output.append({"dir": "wc:" + str(argument) + ": Это каталог"})
                output.append({"file": (0, 0, 0, argument)})
            else:
                output.append(
                    {"dir": "wc: " + str(argument) + ": Нет такого файла или каталога"}
                )
        offset = str((self.max_len // 6 + 1) * 6)
        return output, offset

    def __print_if(self, logic: bool, stdin: str):
        if logic:
            self.__save_stdin(stdin)

    def __save_stdin(self, stdin: str):
        new_lines = len(stdin.strip().split("\n"))
        count = len(stdin.strip().split())
        bytes = len(stdin.encode("utf-8"))
        self.stdout += "{:7d}{:8d}{:8d}".format(new_lines, count, bytes + 1)

    def __is_file(self, name: str):
        return os.path.isfile(name)

    def __is_dir(self, name: str):
        return os.path.isdir(name)

    def __get_info_about_file(self, name_file):
        file = open(name_file, "r")
        new_line, count_words = 0, 0
        while True:
            line = file.readline()
            if not line:
                break
            count_words = count_words + len(line.strip().split())
            if line[-1] == "\n":
                new_line += 1
        size = file.seek(0, os.SEEK_END)
        file.close()
        return new_line, count_words, size
