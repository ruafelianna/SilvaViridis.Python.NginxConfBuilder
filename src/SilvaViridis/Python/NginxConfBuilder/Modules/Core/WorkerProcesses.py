from typing import Literal

from SilvaViridis.Python.Common.Numbers import PositiveInt

from ...Common import DirectiveBase

DIR_WORKER_PROCESSES = "worker_processes"

class WorkerProcesses(DirectiveBase):
    def __init__(
        self,
        order : int,
        quantity : PositiveInt | Literal["auto"] = 1,
    ):
        super().__init__(order, DIR_WORKER_PROCESSES)
        self.add_arg(quantity)
