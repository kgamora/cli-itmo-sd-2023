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
                ans = Executor.exec(executables)
                if ans.code != 0:
                    raise Exception
            except:
                print(ans.stderr)
                return ans.code

    def get_executables(self, stdin: str) -> list[Executable]:
        substitution_cmd = Substituter.substitute(stdin)
        tokens = Lexer.lex(substitution_cmd)
        yield Constructor().construct(tokens)

    def get_context_manager(self):
        return self.context_manager
