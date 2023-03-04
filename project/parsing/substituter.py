import re


class Substituter:

    # Replace names of environment vars in input string
    @staticmethod
    def substitute(token: str) -> str:
        # passing without substitute at part1 of project

        result = tokens_str
        try:
            result = re.sub(r"'(.*)'", r"\1", tokens_str)
        except Exception as e:
            None

        result: str

        if len(token) > 1 and token[0] == "'" and token[-1] == "'":
            result = token[1:-1]
        else:
            result = re.sub(r'"(.*)"', r"\1", token)
            # here needs substitution

        return result

    @staticmethod
    def substitute_all(token_strings: list[str]) -> list[str]:
        # passing without substitute at part1 of project
        for tok in token_strings:
            yield Substituter.substitute(tok)
