from ._DirectivesList import DIR_AUTH_DELAY
from ...Common import DirectiveBase, TimeInterval, TimeIntervalGroup

class AuthDelay(DirectiveBase):
    def __init__(
        self,
        time : TimeInterval | TimeIntervalGroup = TimeInterval(0),
    ):
        super().__init__(DIR_AUTH_DELAY)
        self.add_arg(time)

    @property
    def min_version(
        self,
    ) -> tuple[int, int, int]:
        return (1, 17, 10)
