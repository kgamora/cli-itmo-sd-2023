from project.application.context_manager import ContextManager
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
                executors = self.get_executors(stdin)
                out = None
                for executor in executors:
                    out = executor.exec(out)

            except Exception as e:
                print(type(e))
                break

    def get_executors(self, stdin: str) -> Executable:
        substitution_str = Substituter.substitute(stdin)
        tokens = Lexer.lex(substitution_str)
        return Constructor.construct(tokens)

    def get_context_manager(self):
        return self.context_manager
