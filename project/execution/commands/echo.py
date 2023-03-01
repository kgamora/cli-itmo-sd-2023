from project.execution.executable import Executable


class Echo(Executable):
    def __init__(self):
        super().__init__()

    def execute(self, stdin: str):
        pass
