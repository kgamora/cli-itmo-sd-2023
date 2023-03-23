from project.application.context_manager import ContextManager
from project.execution.executable import Executable


class Assign(Executable):
    def __init__(self, arguments: list[str]):
        super().__init__(arguments)

    def execute(self, stdin: str):
        """
        Executes the command and captures its output (stdout, stderr and return code).
        Behaves in the exact same manner as assigning variable in standard Linux distros.
        :param stdin: command input stream
        :return: None
        """
        ContextManager().set_var(self.arguments[0], self.arguments[1])
        self.ret_code = 0
