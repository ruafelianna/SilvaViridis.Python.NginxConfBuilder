from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup, TimeIntervalUnit

DIR_KEEPALIVE_TIME = "keepalive_time"

class KeepaliveTime(DirectiveBase):
    def __init__(
        self,
        order : int,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(1, TimeIntervalUnit.hours),
    ):
        super().__init__(order, DIR_KEEPALIVE_TIME)
        self.add_arg(time)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 19, 10)
