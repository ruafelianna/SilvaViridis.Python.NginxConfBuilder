from ._DirectivesList import DIR_KEEPALIVE_TIMEOUT
from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

class KeepaliveTimeout(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(75),
        header_time : TimeInterval | TimeIntervalGroup | None = None,
    ):
        super().__init__(DIR_KEEPALIVE_TIMEOUT)
        self.add_arg(time)
        self.add_arg(header_time)
