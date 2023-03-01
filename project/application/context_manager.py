import os

from project.utils.metaclasses import Singleton


class ContextManager(metaclass=Singleton):

    def __init__(self):
        self.var_map: dict[str, str] = {}

    def get_var(self, name_str) -> str:
        if name_str in self.var_map.keys():
            return self.var_map[name_str]
        return os.environ.get(name_str, '')

    def set_var(self, name_str, value_str) -> None:
        self.var_map[name_str] = value_str
