import sys

from project.execution.executable import Executable


class Exit(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)

    def execute(self, stdin: str):
        """
        Executes the command and captures its output (stdout, stderr and return code).
        Behaves in the exact same manner as exit command in standard Linux distros but lacks its flags.
        :param stdin: command input stream
        :return: None
        """
        sys.exit(0)
