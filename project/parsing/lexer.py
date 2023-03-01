from project.parsing.exceptions.LexingException import LexerAssignException


class Lexer:

    # Split input string with spaces and sign '='
    @staticmethod
    def lex(self, tokens_str: str) -> list[str]:
        tokens = tokens_str.split()
        i = 0
        while i < len(tokens):
            new_tokens = tokens[i].split('=')
            if len(new_tokens) > 2:
                raise LexerAssignException()
            if len(new_tokens) > 1:
                tokens = tokens[0:i] + new_tokens[0] + ['='] + new_tokens[1] + tokens + tokens[i + 1:]
        return tokens
