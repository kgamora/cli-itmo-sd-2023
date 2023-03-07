import re
from project.application.context_manager import ContextManager


class Substituter:
    @staticmethod
    def substitute(token: str) -> str:
        """
        Replace variables at "..." with values  from ContextManager.
        Remove "..." and '...'.
        :param token: string
        :return: string with substitution
        """
        # passing without substitute at part1 of project

        result: str

        if len(token) > 1 and token[0] == "'" and token[-1] == "'":
            result = token[1:-1]
        else:
            # here is substitution
            def get_var_value(name):
                v = ContextManager().get_var(str(name)[1:])
                return v

            def find_strings_to_substitute(sub_text):
                v = str(re.sub(r"\$\b\w*", get_var_value, str(sub_text)))
                return v

            result = re.sub(r'"(.*)"', find_strings_to_substitute, result)


        return result

    @staticmethod
    def substitute_all(token_strings: list[str]) -> list[str]:
        """
        Substitutes each element at token_strings and return list of token
        :param token_strings:
        :return: return list of substituted strings
        """
        return list(map(Substituter.substitute, token_strings))
