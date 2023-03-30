import os.path
from project.application.context_manager import ContextManager


def convert_to_abspath(path: str) -> str:
    """
    Convert any path to absolute path.
    Relative path converts to absolute using current working directory from ContextManager;
    Path with home directory like "~/..." expands with home directory;
    Absolute path doesn't change.
    :param path: path to convert
    :return: Absolute path
    """
    expanded_path = os.path.expanduser(path) # expand home dir
    relative_to_cdw = os.path.join(ContextManager().get_cwd(), expanded_path)
    return os.path.abspath(relative_to_cdw)
