import shlex
from project.parsing.exceptions.LexingException import (
    LexerException,
    LexerAssignException,
)


class Lexer:
    @staticmethod
    def lex(tokens_str: str) -> list[str]:
        """
        Split input string with spaces and signs '=', '|' if it not in quotes.
        :param tokens_str: input string
        :return: list of tokens
        """
        try:
            tokens = shlex.split(tokens_str, posix=False)

            i = 0
            while i < len(tokens):
                if (
                    tokens[i][0] == "'"
                    or tokens[i][-1] == "'"
                    or tokens[i][0] == '"'
                    or tokens[i][-1] == '"'
                ):
                    i += 1
                    continue

                new_tokens = tokens[i].split("=")
                if len(new_tokens) > 2:
                    raise LexerAssignException()
                if (
                    len(new_tokens) > 1
                    and len(new_tokens[0]) > 0
                    and len(new_tokens[1]) > 0
                ):
                    tokens = (
                        tokens[0:i]
                        + [new_tokens[0]]
                        + ["="]
                        + [new_tokens[1]]
                        + tokens[i + 1 :]
                    )
                i += 1

        except ValueError as error:
            raise LexerException(error)
        return tokens
