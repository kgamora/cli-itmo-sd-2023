from project.execution.executable import Executable


class Echo(Executable):
    def __init__(self):
        super().__init__()

    @Executable._may_throw
    def execute(self, stdin: str):
        self.stdout = " ".join(self.arguments)
