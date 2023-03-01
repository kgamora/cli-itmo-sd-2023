from abc import ABCMeta, abstractmethod


class Executable(metaclass=ABCMeta):
    def __init__(self):
        self.arguments: list[str]
        self.stdout: str
        self.stderr: str

    @abstractmethod
    def execute(self, stdin: str):
        pass
