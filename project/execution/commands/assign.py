from project.application.context_manager import ContextManager
from project.execution.executable import Executable


class Assign(Executable):
    def __init__(self, arguments: list[str]):
        super().__init__(arguments)

    def execute(self, stdin: str):
        ContextManager().set_var(self.arguments[0], self.arguments[1])
        self.ret_code = 0
