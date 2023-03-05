import os

from project.utils.metaclasses import Singleton


class ContextManager(metaclass=Singleton):
    def __init__(self):
        self.__var_map: dict[str, str] = {}

    # return environment variable
    def get_var(self, name_str) -> str:
        """
        Returns variable by its name.
        :param name_str: name of the variable to get
        :return: value of the variable
        """
        if name_str in self.__var_map.keys():
            return self.__var_map[name_str]
        return os.environ.get(name_str, "")

    def set_var(self, name_str, value_str) -> None:
        """
        Updates or sets context variable name_str to value_str
        :param name_str: name of the variable to set
        :param value_str: value to set
        :return: None
        """
        self.__var_map[name_str] = value_str

    def get_current_env(self) -> dict[str, str]:
        """
        Combines system variables and current context variables and returns them
        :return: dictionary: name to value.
        """
        current_env = os.environ.copy()
        current_env.update(self.__var_map)
        return current_env
