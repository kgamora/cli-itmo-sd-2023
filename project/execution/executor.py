from project.execution.exceptions.exception_exec import ExceptionExec
from project.execution.executable import Executable


class Executor:
    @staticmethod
    def exec(executables: list[Executable]) -> ExceptionExec:
        stdout, stderr, ret_code = None
        for executable in executables:
            executable.execute(stdout)
            stdout = executable.stdout
            stderr = executable.stderr
            ret_code = executable.ret_code
            if ret_code != 0:
                break
        return ExceptionExec(stdout, stderr, ret_code)
