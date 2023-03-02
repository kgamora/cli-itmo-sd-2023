class Substituter:

    # Replace names of environment vars in input string
    @staticmethod
    def substitute(tokens_str: str) -> str:
        # passing without substitute at part1 of project
        return tokens_str

    @staticmethod
    def substitute_all(tokens_strings: list[str]) -> str:
        # passing without substitute at part1 of project
        for tok in tokens_strings:
            yield Substituter.substitute(tok)
