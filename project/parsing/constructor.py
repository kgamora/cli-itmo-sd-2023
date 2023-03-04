from project.execution.commands.assign import Assign
from project.execution.commands.cat import Cat
from project.execution.commands.wc import WC
from project.execution.executable import Executable
from project.execution.commands.global_executable import GlobalExecutor
from project.execution.commands.echo import Echo
from project.execution.commands.pwd import PWD
from project.execution.commands.exit import Exit


class Constructor:
    def __init__(self):
        """
        Private methods to construct Executable with 'name'
            must be named "_construct_'name'"
        """
        self._executable_constructions_keyword = "_construct_"
        self.map_of_executables: dict = {}
        for k in self.__dir__():
            if k.startswith(self._executable_constructions_keyword):
                self.map_of_executables[
                    k.removeprefix(self._executable_constructions_keyword)
                ] = getattr(self, k)

    def construct(self, tokens_list: list[str]) -> Executable | None:
        """
        Constructs from list of tokens instance of Executable
        :param tokens_list: input list of tokens
        :return: Executable
        """
        if len(tokens_list) == 0:
            return None
        if len(tokens_list) > 1 and tokens_list[1] == "=":
            return Assign(tokens_list[0:1] + tokens_list[2:])

        if tokens_list[0] in self.map_of_executables.keys():
            return self.map_of_executables[tokens_list[0]](tokens_list[1:])
        else:
            return self._construct_global_executable(tokens_list)

    def construct_all(self, tokens_lists: list[list[str]]) -> list[Executable | None]:
        """
        Construct several Executable from list of strings.
        :param tokens_lists:
        :return: list of Executable
        """
        if len(tokens_lists) == 0:
            return []
        for tokens_list in tokens_lists:
            yield self.construct(tokens_list)

    def _construct_global_executable(self, tokens_list: list[str]):
        return GlobalExecutor(tokens_list)

    def _construct_echo(self, tokens_list: list[str]):
        return Echo(tokens_list)

    def _construct_pwd(self, tokens_list: list[str]):
        return PWD(tokens_list)

    def _construct_exit(self, tokens_list: list[str]):
        return Exit(tokens_list)

    def _construct_wc(self, tokens: list[str]):
        return WC(tokens)

    def _construct_cat(self, tokens: list[str]):
        return Cat(tokens)
