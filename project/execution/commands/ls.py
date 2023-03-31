from project.execution.executable import Executable
from os import scandir
from os.path import sep as os_sep
from project.utils.fileutils import convert_to_abspath
from project.application.context_manager import ContextManager


class LS(Executable):
    def __init__(self, arguments: list[str] | None = None):
        super().__init__(arguments)

    @Executable._may_throw
    def execute(self, stdin: str):
        """
        Executes the command and captures its output (stdout, stderr and return code).
        Behaves in the exact same manner as ls command in standard bash lacks its flags.
        :param stdin: command input stream
        :return: None
        """
        if self.arguments == None:
            dir = ContextManager().get_cwd()
        else:
            try:
                dir = convert_to_abspath(stdin)
            except Exception as ex:
                self.stderr += f"ls: cannot access '{dir}': No such file or directory\n"
                self.ret_code = 2
                return

        self.stdout = ""
        entries = [
            x.name + os_sep if x.is_dir() else x.name
            for x in scandir(convert_to_abspath(dir))
        ]
        entries = list(filter(lambda x: not x.startswith("."), entries))
        entries.sort(key=lambda v: v.upper())

        for e in entries:
            if len(self.stdout) > 0:
                self.stdout += " "
            self.stdout += e
        self.ret_code = 0
