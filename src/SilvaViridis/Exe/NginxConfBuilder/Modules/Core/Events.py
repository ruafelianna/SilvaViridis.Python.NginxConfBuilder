from collections.abc import Sequence

from .Include import Include
from .WorkerConnections import WorkerConnections
from ...Common import DirectiveBase

DIR_EVENTS = "events"

class Events(DirectiveBase):
    def __init__(
        self,
        order : int,
        include_list : Sequence[Include] = [],
        worker_connections : WorkerConnections | None = None,
    ):
        super().__init__(order, DIR_EVENTS)

        for include in include_list:
            self.add_directive(include)

        self.add_directive(worker_connections)
