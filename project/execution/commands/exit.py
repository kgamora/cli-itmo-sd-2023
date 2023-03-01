from project.execution.executable import Executable


class Exit(Executable):
    def __init__(self):
        super().__init__()

    def execute(self, stdin: str):
        pass
