from typing import Literal

from SilvaViridis.Python.Common.Types import PositiveInt

from ._DirectivesList import DIR_WORKER_PROCESSES
from ...Common import DirectiveBase

class WorkerProcesses(DirectiveBase):
    def __init__(
        self,
        quantity : PositiveInt | Literal["auto"] = 1,
    ):
        super().__init__(DIR_WORKER_PROCESSES)
        self.add_arg(quantity)
