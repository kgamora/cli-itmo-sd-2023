from project.execution.executable import Executable


class Echo(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)

    @Executable._may_throw
    def execute(self, stdin: str):
        self.stdout = " ".join(self.arguments)
