from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

DIR_KEEPALIVE_MIN_TIMEOUT = "keepalive_min_timeout"

class KeepaliveMinTimeout(DirectiveBase):
    def __init__(
        self,
        order : int,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(0),
    ):
        super().__init__(order, DIR_KEEPALIVE_MIN_TIMEOUT)
        self.add_arg(time)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 27, 4)
