from collections.abc import Sequence

from .Core import (
    ErrorLog,
    Include,
    Pid,
    User,
    WorkerProcesses,
)
from .HttpCore import (
    Http,
)
from ..Common import DirectiveBase

class MainContext(DirectiveBase):
    def __init__(
        self,
        error_log : ErrorLog | None = None,
        include_list : Sequence[Include] = [],
        http : Http | None = None,
        pid : Pid | None = None,
        user : User | None = None,
        worker_processes : WorkerProcesses | None = None,
    ):
        super().__init__("main")
        self.add_directive(error_log)

        for include in include_list:
            self.add_directive(include)

        self.add_directive(http)
        self.add_directive(pid)
        self.add_directive(user)
        self.add_directive(worker_processes)
