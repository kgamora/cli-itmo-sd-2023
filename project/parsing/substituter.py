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

        result: str = token

        if len(token) > 1 and token[0] == "'" and token[-1] == "'":
            result = token[1:-1]
        else:
            result = re.sub(r'"(.*)"', r"\1", token)

            # here is substitution
            def get_var_value(name: re.Match):
                key = name[0]
                v = ContextManager().get_var(key[1:])
                return v[0:]

            def find_strings_to_substitute(sub_text):
                v = re.sub(r"(\$\b\w*)", get_var_value, sub_text)
                s = sub_text
                return str(v[0:])
            #

            result = re.sub(r'(\$\b\w*)', get_var_value, result)
            # result = str(re.sub(r'"(.*)"', r"\1", token))

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
