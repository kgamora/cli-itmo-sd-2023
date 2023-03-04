from project.execution.executor_report import ExecutorReport
from project.execution.executable import Executable


class Executor:
    @staticmethod
    def exec(executables: list[Executable]) -> ExecutorReport:
        """
        Get list of Executable and executes it redirected output of previous to input next
        :param executables: list of Executable to run
        :return: ExecutionReport of the last successful execution
        """
        report = ExecutorReport("", "", 0)
        for executable in executables:
            executable.execute(report.stdout)
            report = ExecutorReport(
                executable.stdout, executable.stderr, executable.ret_code
            )
            if report.ret_code != 0:
                break
        return report
