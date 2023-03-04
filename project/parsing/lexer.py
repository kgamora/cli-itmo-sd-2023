import shlex
from project.parsing.exceptions.LexingException import LexerException


class Lexer:
    @staticmethod
    def lex(tokens_str: str) -> list[str]:
        """
        Split input string with spaces and signs '=', '|' if it not in quotes.
        :param tokens_str: input string
        :return: list of tokens
        """
        try:
            result = shlex.split(tokens_str, posix=False)
        except ValueError as error:
            raise LexerException(error)
        return result
