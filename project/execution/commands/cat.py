from project.execution.executable import Executable


class Cat(Executable):
    def __init__(self, arguments: list[str] | None = []):
        super().__init__(arguments)

    @Executable._may_throw
    def execute(self, stdin: str = ""):
        """
        Executes the command and captures its output (stdout, stderr and return code).
        Concatenate files to stdout like cat command in standard Linux distros but lacks its flags.
        :param stdin: command input stream
        :return: None
        """
        if not self.arguments:
            self.stdout += stdin
        else:
            for file_name in self.arguments:
                with open(file_name) as file:
                    self.stdout += "".join([line for line in file])
        self.ret_code = 0
