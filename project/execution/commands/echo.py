from project.execution.executable import Executable


class Echo(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)

    @Executable._may_throw
    def execute(self, stdin: str):
        """
        Executes the command and captures its output (stdout, stderr and return code).
        Behaves in the exact same manner as echo command in standard Linux distros but lacks its flags.
        :param stdin: command input stream
        :return: None
        """
        self.stdout = " ".join(self.arguments)
        self.ret_code = 0