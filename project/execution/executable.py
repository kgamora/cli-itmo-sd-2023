from abc import ABCMeta, abstractmethod


class Executable(metaclass=ABCMeta):
    def __init__(self, arguments: list[str] | None):
        self.arguments: list[str] | None = arguments
        self.stdout: str | None = ""
        self.stderr: str | None = ""
        self.ret_code: int | None = None

    @abstractmethod
    def execute(self, stdin: str) -> None:
        """
        Executes the command and captures its output (stdout, stderr and return code).
        :param stdin: command input stream
        :return: None
        """
        pass

    def _may_throw(execution: callable):
        def wrapper(self: Executable, stdin: str = ""):
            try:
                execution(self, stdin)
            except BaseException as e:
                self.stderr += str(e)
                self.ret_code = 2

        return wrapper
