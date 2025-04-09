from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

DIR_KEEPALIVE_TIMEOUT = "keepalive_timeout"

class KeepaliveTimeout(DirectiveBase):
    def __init__(
        self,
        order : int,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(value = 75),
        header_time : TimeInterval | TimeIntervalGroup | None = None,
    ):
        super().__init__(order, DIR_KEEPALIVE_TIMEOUT)
        self.add_arg(time)
        self.add_arg(header_time)
