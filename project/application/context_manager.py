from project.utils.metaclasses import Singleton


class ContextManager(metaclass=Singleton):

    def get_var(self, name_str) -> str:
        pass

    def set_var(self, name_str, value_str) -> None:
        pass
