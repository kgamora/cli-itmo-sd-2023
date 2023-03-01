from project.execution.executable import Executable


class GlobalExecutor(Executable):

    def __init__(self):
        super().__init__()
        self.system_process = None

    def execute(self, stdin: str):
        pass
