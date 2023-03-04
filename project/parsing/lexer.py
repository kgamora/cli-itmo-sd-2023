from project.parsing.exceptions.LexingException import LexerAssignException
import shlex


class Lexer:

    # Split input string with spaces and signs '=', '|'
    @staticmethod
    def lex(tokens_str: str) -> list[str]:
        return shlex.split(tokens_str, posix=False)
