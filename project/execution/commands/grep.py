from project.execution.executable import Executable
import argparse


class Grep(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)
        self.args = self._init_args()

    def _init_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-w', default=None)
        parser.add_argument('-A', default=None)
        parser.add_argument('-i', action='store_const', default=False, const=True)
        return parser.parse_args(self.arguments)

    @Executable._may_throw
    def execute(self, stdin: str):
        """
        Executes the command and captures its output (stdout, stderr and return code).
        Behaves in the exact same manner as echo command in standard Linux distros but lacks its flags.
        :param stdin: command input stream
        :return: None
        """
        print(self.args)
        self.stdout = " ".join(self.arguments)
        self.ret_code = 0

#
# test = Grep(["-w", "word", "-A", "10"])
#
# test.execute(None)
