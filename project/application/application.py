from project.application.context_manager import ContextManager
from project.execution.executor import Executor
from project.parsing.constructor import Constructor
from project.parsing.lexer import Lexer
from project.parsing.substituter import Substituter
from project.utils.metaclasses import Singleton
from project.execution.executable import Executable


class Application(metaclass=Singleton):
    def __init__(self) -> None:
        self.context_manager = ContextManager()

    def run(self):
        while True:
            try:
                stdin = input()
                executables = self.get_executables(stdin)
                Executor.exec(executables)

            except Exception as e:
                print(type(e))
                break

    def get_executables(self, stdin: str) -> list[Executable]:
        substitution_cmd = Substituter.substitute(stdin)
        tokens = Lexer.lex(substitution_cmd)
        executables = []
        for token in tokens:
            executables.append(Constructor.construct(tokens))
        return executables

    def get_context_manager(self):
        return self.context_manager
