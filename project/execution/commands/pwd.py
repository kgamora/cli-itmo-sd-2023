import os

from project.execution.executable import Executable


class PWD(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)

    @Executable._may_throw
    def execute(self, stdin: str):
        self.stdout = os.getcwd()
