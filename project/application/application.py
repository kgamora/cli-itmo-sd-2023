from project.application.context_manager import ContextManager
from project.execution.executor import Executor
from project.parsing.constructor import Constructor
from project.parsing.lexer import Lexer
from project.parsing.substituter import Substituter
from project.utils.metaclasses import Singleton
from project.execution.executable import Executable
from project.utils.parserutils import split


class Application(metaclass=Singleton):
    _STDERROR_COLOR_BEGIN = "\033[91m"
    _STDERROR_COLOR_END = "\033[0m"

    def __init__(self):
        self.context_manager = ContextManager()

    def run(self):
        """
        Read-Execute-Print Loop
        :return:
        """
        while True:
            try:
                stdin = input()
                executables = self.get_executables(stdin)
                report = Executor.exec(executables)
                if report.stdout and len(report.stdout) > 0:
                    print(report.stdout)
                if report.stderr and len(report.stderr) > 0:
                    print(
                        self._STDERROR_COLOR_BEGIN,
                        report.stderr,
                        self._STDERROR_COLOR_END,
                    )
            except KeyboardInterrupt:
                exit(0)
            except Exception as e:
                print(e)

    def get_executables(self, stdin: str) -> list[Executable]:
        """
        Converts input string to list of Executables
        :param stdin: user input to parse
        :return: list of commands to execute
        """
        tokens: list[str] = Lexer.lex(stdin)
        substituted_tokens: list[str] = Substituter.substitute_all(tokens)
        substituted_tokens_list: list[str] = split(substituted_tokens, "|")

        # Here need add splitting tokens by pipes
        # And insert construction at cycle

        constructor = Constructor()
        for substituted_tokens in substituted_tokens_list:
            executable = constructor.construct(substituted_tokens)
            if executable:
                yield executable

    def get_context_manager(self):
        return self.context_manager
