import subprocess

from project.execution.executable import Executable
from subprocess import CompletedProcess


class GlobalExecutor(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)
        self.system_process = None

    @Executable._may_throw
    def execute(self, stdin: str):
        """
        Executes the command and captures its output (stdout, stderr and return code).
        :param stdin: command input stream
        :return: None
        """
        completedProcess: CompletedProcess = subprocess.run(
            args=self.arguments, capture_output=True, universal_newlines=True
        )
        self.ret_code, self.stdout, self.stderr = (
            completedProcess.returncode,
            completedProcess.stdout,
            completedProcess.stderr,
        )
