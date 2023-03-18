import shlex
from abc import ABCMeta, abstractmethod

from project.parsing.exceptions.LexingException import (
    LexerException,
    LexerAssignException,
)


class LexerAction(metaclass=ABCMeta):
    @abstractmethod
    def perform(self, tokens: list[str]) -> list[str]:
        """
        Auxiliary lexing method. Performs one of the lexing stages.
        :param tokens: list of tokens
        :return: list of tokens
        """
        pass

    @staticmethod
    def is_string(line):
        return line[0] == "'" and line[-1] == "'" or line[0] == '"' and line[-1] == '"'


class SeparateAssign(LexerAction):
    def perform(self, tokens: list[str]):
        """
        Auxiliary lexing method. Performs separation by equals sign.
        :param tokens: list of tokens
        :return: list of tokens
        """
        i = 0
        while i < len(tokens):
            if self.is_string(tokens[i]):
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
                    tokens[0:i] + [new_tokens[0], "=", new_tokens[1]] + tokens[i + 1 :]
                )
            i += 1

        return tokens


class SeparatePipe(LexerAction):
    pipe = "|"

    def perform(self, tokens: list[str]):
        """
        Auxiliary lexing method. Performs separation by pipe sign.
        :param tokens: list of tokens
        :return: list of tokens
        """
        i = 0
        while i < len(tokens):
            if self.is_string(tokens[i]) or tokens[i] == self.pipe:
                i += 1
                continue

            new_tokens = tokens[i].split(self.pipe)
            if len(new_tokens) > 2:
                raise LexerAssignException()
            if len(new_tokens) > 1:
                median = [new_tokens[0]] if len(new_tokens[0]) > 0 else []
                for tok in new_tokens[1:]:
                    median += [self.pipe, tok] if len(tok) > 0 else [self.pipe]
                tokens = tokens[0:i] + median + tokens[i + 1 :]
                continue
            i += 1
        return tokens


class Lexer:
    _actions = [SeparateAssign(), SeparatePipe()]

    def __init__(self, actions: list[LexerAction] = None):
        if actions:
            self.actions = actions
        else:
            self.actions = Lexer._actions

    @classmethod
    def lex(cls, tokens_str: str) -> list[str]:
        """
        Split the input string by whitespace and '=', '|' signs if it is not surrounded with single-quotes.
        :param tokens_str: input string
        :return: list of tokens
        """
        try:
            tokens = shlex.split(tokens_str, posix=False)
        except ValueError as error:
            raise LexerException(error)

        for action in cls._actions:
            tokens = action.perform(tokens)

        return tokens
