from project.execution.executable import Executable


class GlobalExecutor(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)
        self.system_process = None

    def execute(self, stdin: str):
        pass
