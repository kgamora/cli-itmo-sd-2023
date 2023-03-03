import os

from project.execution.executable import Executable


class WC(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)

    @Executable._may_throw
    def execute(self, stdin: str = ""):
        """
        Executes the command and captures its output (stdout, stderr and return code).
        Behaves in the exact same manner as wc command in standard Linux distros but lacks its flags.
        :param stdin: command input stream
        :return: None
        """
        self.__print_if(stdin and len(stdin) != 0, stdin)
        max_len, total_line, total_word, total_byte = 0, 0, 0, 0
        output = []
        for argument in self.arguments:
            if self.__is_file(argument):
                count_new_line, count_words, size = self.__get_info_about_file(argument)
                total_line += count_new_line
                total_word += count_words
                total_byte += size
                max_len = max(max_len, len(str(total_byte)))
                output.append({"file": (count_new_line, count_words, size, argument)})
            elif self.__is_dir(argument):
                output.append({"dir": "wc:" + str(argument) + ": Это каталог"})
                output.append({"file": (0, 0, 0, argument)})
        offset = str((max_len // 2 + 1) * 2)
        template = (
            "{:" + offset + "d}{:" + offset + "d}{:" + offset + "d} {:" + offset + "s}"
        )
        for out in output:
            if "dir" in out:
                print(out["dir"])
            if "file" in out:
                print(template.format(*out["file"]))
        if len(self.arguments) != 1:
            print(template.format(total_line, total_word, total_byte, "итого"))

    def __print_if(self, logic: bool, stdin: str):
        if logic:
            self.__print_stdin(stdin)

    def __print_stdin(self, stdin: str):
        count = len(stdin.strip().split())
        bytes = len(stdin.encode("utf-8"))
        print("{:8d}{:8d}{:8d}".format(1, count, bytes + 1))

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
