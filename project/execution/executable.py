from abc import ABCMeta, abstractmethod


class Executable(metaclass=ABCMeta):
    def __init__(self):
        self.arguments: list[str]
        self.stdout: str
        self.stderr: str

    @abstractmethod
    def execute(self, stdin: str):
        pass

    def _may_throw(execution: callable):
        def wrapper(self: Executable, stdin: str):
            try:
                execution(self, stdin)
            except BaseException as e:
                self.stderr = str(e)

        return wrapper
