from project.parsing.exceptions.LexingException import LexerAssignException


class Lexer:

    # Split input string with spaces and signs '=', '|'
    @staticmethod
    def lex(tokens_str: str) -> list[str]:
        return shlex.split(tokens_str, posix=False)
