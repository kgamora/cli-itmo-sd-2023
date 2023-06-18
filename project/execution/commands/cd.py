import os
from project.application.context_manager import ContextManager

from project.execution.executable import Executable
from project.utils.fileutils import convert_to_abspath


class CD(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)

    @Executable._may_throw
    def execute(self, stdin: str):
        """
        Executes the command and captures its output (stdout, stderr and return code).
        Behaves in the exact same manner as pwd command in standard Linux distros but lacks its flags.
        :param stdin: command input stream
        :return: None
        """
        self.stdout = ""
        self.stderr = ""
        self.ret_code = 0
        if not self.arguments:
            abs_path = os.path.expanduser("~")
        else:
            abs_path = convert_to_abspath(self.arguments[0])

            if len(self.arguments) > 1:
                self.stderr += "Ожидался один аргумент\n"
                self.ret_code = 1
            elif not os.path.exists(abs_path):
                self.stderr += f"Нет такого файла или директории: {self.arguments[0]}\n"
                self.ret_code = 2
            elif not os.path.isdir(abs_path):
                self.stderr += f"Не директория: {self.arguments[0]}\n"
                self.ret_code = 3

        if self.ret_code == 0:
            ContextManager().set_cwd(abs_path)
