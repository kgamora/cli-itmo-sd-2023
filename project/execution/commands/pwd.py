import os
from project.application.context_manager import ContextManager

from project.execution.executable import Executable


class PWD(Executable):
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
        self.stdout = ContextManager().get_cwd()
        self.ret_code = 0
