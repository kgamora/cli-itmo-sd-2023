import os

from project.execution.executable import Executable


class PWD(Executable):
    def __init__(self):
        super().__init__()

    @Executable._may_throw
    def execute(self, stdin: str):
        self.stdout = os.getcwd()
