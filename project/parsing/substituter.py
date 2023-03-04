import re


class Substituter:

    # Replace names of environment vars in input string
    @staticmethod
    def substitute(tokens_str: str) -> str:
        # passing without substitute at part1 of project

        result = tokens_str
        try:
            result = re.sub(r"'(.*)'", r"\1", tokens_str)
        except Exception as e:
            None

        result: str

        if len(tokens_str) > 1 and tokens_str[0] == "'" and tokens_str[-1] == "'":
            result = tokens_str[1:-1]
        else:
            result = re.sub(r'"(.*)"', r"\1", tokens_str)
            # here needs substitution

        return result

    @staticmethod
    def substitute_all(token_strings: list[str]) -> list[str]:
        # passing without substitute at part1 of project
        for tok in tokens_strings:
            yield Substituter.substitute(tok)
