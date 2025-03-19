from ._DirectivesList import DIR_KEEPALIVE_TIME
from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup, TimeIntervalUnit

class KeepaliveTime(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(1, TimeIntervalUnit.hours),
    ):
        super().__init__(DIR_KEEPALIVE_TIME)
        self.add_arg(time)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 19, 10)
