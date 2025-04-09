from SilvaViridis.Python.Common.Numbers import PositiveInt

from ...Common import DirectiveBase

DIR_WORKER_CONNECTIONS = "worker_connections"

class WorkerConnections(DirectiveBase):
    def __init__(
        self,
        order : int,
        quantity : PositiveInt = 512,
    ):
        super().__init__(order, DIR_WORKER_CONNECTIONS)
        self.add_arg(quantity)
