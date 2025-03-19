from ._DirectivesList import DIR_KEEPALIVE_MIN_TIMEOUT
from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

class KeepaliveMinTimeout(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(0),
    ):
        super().__init__(DIR_KEEPALIVE_MIN_TIMEOUT)
        self.add_arg(time)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 27, 4)
