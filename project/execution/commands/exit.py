import sys

from project.execution.executable import Executable


class Exit(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)

    def execute(self, stdin: str):
        sys.exit(0)
